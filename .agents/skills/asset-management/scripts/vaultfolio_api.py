#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_BASES = [
    "http://api:18087",
    "http://vaultfolio-api:18087",
    "http://192.168.5.215:18087",
    "http://127.0.0.1:18087",
    "http://127.0.0.1:18088",
]


def fetch_json(base, path, timeout=8):
    with urllib.request.urlopen(base.rstrip("/") + path, timeout=timeout) as response:
        return json.load(response)


def resolve_base(explicit):
    candidates = []
    if explicit:
        candidates.append(explicit)
    env_base = os.environ.get("VAULTFOLIO_API_BASE")
    if env_base:
        candidates.append(env_base)
    candidates.extend(DEFAULT_BASES)

    seen = set()
    for base in candidates:
        if base in seen:
            continue
        seen.add(base)
        try:
            payload = fetch_json(base, "/api/health", timeout=5)
        except (OSError, urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            continue
        if payload.get("success") and payload.get("data", {}).get("status") == "ok":
            return base, payload
    raise SystemExit("Vaultfolio API is unreachable from this session")


def data_items(payload):
    return payload.get("data", {}).get("items", [])


def filter_query(items, query):
    if not query:
        return items
    pattern = re.compile(query, re.IGNORECASE)
    return [
        item
        for item in items
        if pattern.search(json.dumps(item, ensure_ascii=False))
    ]


def cmd_positions(base, args):
    payload = fetch_json(base, "/api/positions")
    payload["data"]["items"] = filter_query(data_items(payload), args.query)
    return payload


def cmd_market_positions(base, args):
    payload = fetch_json(base, "/api/market/positions")
    payload["data"]["items"] = filter_query(data_items(payload), args.query)
    return payload


def cmd_dashboard_summary(base, _args):
    payload = fetch_json(base, "/api/dashboard")
    data = payload.get("data", {})
    return {
        "success": payload.get("success"),
        "message": payload.get("message"),
        "data": {
            "overview": data.get("overview"),
            "allocation": data.get("allocation"),
        },
    }


def cmd_reports(base, args):
    payload = fetch_json(base, "/api/analysis/reports")
    items = filter_query(data_items(payload), args.query)
    if args.compact:
        items = [
            {
                "id": item.get("id"),
                "referenceId": item.get("referenceId"),
                "taskKey": item.get("taskKey"),
                "title": item.get("title"),
                "summary": item.get("summary"),
                "status": item.get("status"),
                "createdAt": item.get("createdAt"),
                "recommendations": item.get("recommendations", []),
            }
            for item in items
        ]
    payload["data"]["items"] = items
    return payload


def cmd_research_candidates(base, args):
    status = urllib.parse.quote(args.status)
    payload = fetch_json(base, f"/api/market/research-candidates?status={status}")
    payload["data"]["items"] = filter_query(data_items(payload), args.query)
    return payload


def main():
    parser = argparse.ArgumentParser(description="Read-only Vaultfolio API helper")
    parser.add_argument("--base", help="Vaultfolio API base URL")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("health")
    p = sub.add_parser("positions")
    p.add_argument("--query", default="")
    p = sub.add_parser("market-positions")
    p.add_argument("--query", default="")
    sub.add_parser("dashboard-summary")
    sub.add_parser("cash-balances")
    p = sub.add_parser("reports")
    p.add_argument("--query", default="")
    p.add_argument("--compact", action="store_true")
    p = sub.add_parser("research-candidates")
    p.add_argument("--status", default="all")
    p.add_argument("--query", default="")
    p = sub.add_parser("position-options")
    p.add_argument("query")

    args = parser.parse_args()
    base, health = resolve_base(args.base)
    handlers = {
        "health": lambda: health,
        "positions": lambda: cmd_positions(base, args),
        "market-positions": lambda: cmd_market_positions(base, args),
        "dashboard-summary": lambda: cmd_dashboard_summary(base, args),
        "cash-balances": lambda: fetch_json(base, "/api/cash-balances"),
        "reports": lambda: cmd_reports(base, args),
        "research-candidates": lambda: cmd_research_candidates(base, args),
        "position-options": lambda: fetch_json(
            base,
            "/api/analysis/parameter-options?source=current_positions&q="
            + urllib.parse.quote(args.query),
        ),
    }
    print(json.dumps(handlers[args.command](), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as exc:
        print(f"Vaultfolio API HTTP error: {exc.code}", file=sys.stderr)
        sys.exit(1)
