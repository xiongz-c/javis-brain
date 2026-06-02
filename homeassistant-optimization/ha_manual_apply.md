# Home Assistant Manual Apply Plan

This plan avoids disabling entities. It creates cleaner daily controls while keeping all raw entities visible to Jarvis through the Home Assistant API.

## 1. Add Switch-Backed Lights

Add the switch-backed light wrappers to Home Assistant's YAML configuration.

Recommended structure:

```yaml
# configuration.yaml
light: !include lights_template_wrappers.yaml
```

Then copy `lights_template_wrappers.yaml` into the same directory as `configuration.yaml`.

Alternative: if you prefer a single file, copy the complete top-level snippet from `suggested_template_lights.yaml` into `configuration.yaml`.

If `configuration.yaml` already has a `light:` section, merge the template platform into the existing section instead of adding a second top-level `light:` key.

After saving:

1. Go to Home Assistant: Settings -> System -> Repairs -> three-dot menu -> Check configuration.
2. If valid, restart Home Assistant or reload YAML integrations if your setup supports it.
3. Ask Jarvis to verify that these entities exist:
   - `light.kitchen_main_light`
   - `light.dining_wall_light`
   - `light.dining_table_light`
   - `light.hallway_firework_light`
   - `light.living_room_spotlight_switched`
   - `light.balcony_ceiling_light`
   - `light.bedroom_wall_light`
   - `light.bedroom_ceiling_light`
   - `light.study_ceiling_light`
   - `light.bathroom_mirror_light`

## 2. Daily Dashboard Principle

Do not disable Xiaomi/Home Assistant auxiliary entities. Some are useful for Jarvis diagnostics, maintenance checks, and anomaly detection.

For human-facing dashboards, show only:

- Daily control lights and grouped lights
- Climate devices
- Curtains/covers
- Ordinary plugs
- Vacuum main control
- A small maintenance section for genuinely useful health/fault signals

Hide from dashboard by omission:

- `number.*`
- `select.*`
- `button.*`
- `event.*`
- `notify.*`
- Entities with names containing `自定义属性`, `设置模式`, `遥控地址`, `情景模式`, `学习上报`, `清除配对`, `清除互控`

These entities remain visible to Jarvis through `/api/states`.

## 3. Grouped Downlight Semantics

Use group entities for daily control:

- 厨房筒灯: `light.mijia_cn_group_1978090431347445760_group3_s_2_light`
- 浴室外筒灯: `light.mijia_cn_group_1978088695174021121_group3_s_2_light`
- 电视墙射灯: `light.mijia_cn_group_1978089154580332544_group3_s_2_light`

Individual 平头熊 downlights remain visible for diagnostics and repair, but Jarvis should not use them as the default when the user asks to control room/group lighting.

## 4. Jarvis Validation Prompt

After adding the template lights and restarting/reloading Home Assistant, ask:

```text
@Jarvis🐻 验证 Home Assistant 里这 10 个 template light 是否已经出现，并检查厨房筒灯、浴室外筒灯、电视墙射灯是否优先按组控制
```
