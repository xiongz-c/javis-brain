const fs = require('fs');

const haUrl = process.env.HOME_ASSISTANT_URL || 'http://homeassistant:8123';
const token = process.env.HOME_ASSISTANT_TOKEN;

if (!token) {
  console.error('HOME_ASSISTANT_TOKEN is not set.');
  process.exit(1);
}

const expectedTemplateLights = [
  'light.kitchen_main_light',
  'light.dining_wall_light',
  'light.dining_table_light',
  'light.hallway_firework_light',
  'light.living_room_spotlight_switched',
  'light.balcony_ceiling_light',
  'light.bedroom_wall_light',
  'light.bedroom_ceiling_light',
  'light.study_ceiling_light',
  'light.bathroom_mirror_light',
];

const preferredGroupLights = [
  'light.mijia_cn_group_1978090431347445760_group3_s_2_light',
  'light.mijia_cn_group_1978088695174021121_group3_s_2_light',
  'light.mijia_cn_group_1978089154580332544_group3_s_2_light',
];

async function main() {
  const res = await fetch(`${haUrl}/api/states`, {
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
  });
  if (!res.ok) {
    throw new Error(`Home Assistant API failed: ${res.status} ${await res.text()}`);
  }
  const states = await res.json();
  const ids = new Set(states.map((state) => state.entity_id));

  const missingTemplateLights = expectedTemplateLights.filter((id) => !ids.has(id));
  const presentTemplateLights = expectedTemplateLights.filter((id) => ids.has(id));
  const missingGroupLights = preferredGroupLights.filter((id) => !ids.has(id));

  const semantics = fs.readFileSync('/workspaces/homeassistant-optimization/home_semantics_core.yaml', 'utf8');
  const referencedExistingEntities = [...semantics.matchAll(/(?:entity_id|backing_entity): "([^"]+)"/g)]
    .map((match) => match[1])
    .filter((id) => !expectedTemplateLights.includes(id));
  const missingReferencedEntities = referencedExistingEntities.filter((id) => !ids.has(id));

  console.log(JSON.stringify({
    checked_at: new Date().toISOString(),
    template_lights: {
      expected: expectedTemplateLights.length,
      present: presentTemplateLights,
      missing: missingTemplateLights,
    },
    preferred_group_lights: {
      expected: preferredGroupLights,
      missing: missingGroupLights,
    },
    semantics_core: {
      referenced_existing_entities: referencedExistingEntities.length,
      missing_referenced_entities: missingReferencedEntities,
    },
    ok: missingTemplateLights.length === 0
      && missingGroupLights.length === 0
      && missingReferencedEntities.length === 0,
  }, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
