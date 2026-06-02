# Home Assistant Entity Audit

Generated: 2026-05-30T16:22:21.468Z

## Summary

- Total states from HA: 1491
- Registry entities currently present in states: 1488
- HA version: 2025.5.3

### Domain Counts

| Domain | Count |
| --- | --- |
| number | 340 |
| switch | 212 |
| button | 198 |
| sensor | 191 |
| select | 155 |
| event | 152 |
| notify | 128 |
| text | 39 |
| light | 30 |
| binary_sensor | 24 |
| media_player | 3 |
| remote | 3 |
| climate | 3 |
| update | 2 |
| cover | 2 |
| conversation | 1 |
| zone | 1 |
| person | 1 |
| sun | 1 |
| todo | 1 |
| tts | 1 |
| weather | 1 |
| vacuum | 1 |
| fan | 1 |

### Recommendation Counts

| Recommendation | Count |
| --- | --- |
| hide_or_disable_aux | 1159 |
| keep_sensor_review | 182 |
| review | 94 |
| keep_primary | 31 |
| keep_but_label_indicator | 12 |
| wrap_as_light | 10 |

## Switches That Should Probably Become Lights

| Area | Name | Proposed Name | Entity | State |
| --- | --- | --- | --- | --- |
| 餐厨 | 餐厨开关（三键） 厨房灯 左键 | 厨房灯 | switch.linp_cn_2002626186_t2dbw3_on_p_2_1 | on |
| 餐厨 | 餐厨开关（三键） 餐厅壁灯 中键 | 餐厅壁灯 | switch.linp_cn_2002626186_t2dbw3_on_p_3_1 | off |
| 餐厨 | 餐厨开关（三键） 餐桌灯 右键 | 餐桌灯 | switch.linp_cn_2002626186_t2dbw3_on_p_4_1 | off |
| 走廊 | 左键-走廊开关 烟花灯 中键 | 烟花灯 | switch.linp_cn_2002874216_t2dbw3_on_p_3_1 | on |
| 走廊 | 左键-走廊开关 客厅射灯 右键 | 客厅射灯 | switch.linp_cn_2002874216_t2dbw3_on_p_4_1 | on |
| 阳台 | 阳台开关 吸顶灯 左键 | 阳台吸顶灯 | switch.linp_cn_2021957403_t2dbw2_on_p_2_1 | off |
| 主卧 | 主卧开关（双键） 壁灯 左键 | 主卧壁灯 | switch.linp_cn_2022408943_t2dbw2_on_p_2_1 | off |
| 主卧 | 主卧开关（双键） 吸顶灯 右键 | 主卧吸顶灯 | switch.linp_cn_2022408943_t2dbw2_on_p_3_1 | off |
| 书房 | 书房开关（双键） 吸顶灯 左键 | 书房吸顶灯 | switch.linp_cn_2022388066_t2dbw2_on_p_2_1 | on |
| 浴室 | 浴室镜灯 开关 开关状态 | 浴室镜灯 开关 开关状态 | switch.giot_cn_2022913171_v9icm_on_p_2_1 | off |

## Native Lights To Keep As Primary Controls

| Area | Name | Entity | State |
| --- | --- | --- | --- |
| 客厅 | 平头熊F1调光筒射灯(Mesh2.0) 4 灯 | light.090615_cn_2022122260_milg05_s_2_light | off |
| 客厅 | 平头熊F1调光筒射灯(Mesh2.0) 3 灯 | light.090615_cn_2041348683_milg05_s_2_light | off |
| 客厅 | 平头熊F1调光筒射灯(Mesh2.0) 2 灯 | light.090615_cn_947717173_milg05_s_2_light | off |
| 客厅 | 平头熊F1调光筒射灯(Mesh2.0) 灯 | light.090615_cn_947770195_milg05_s_2_light | off |
| 电视墙 | 电视墙射灯 灯 | light.mijia_cn_group_1978089154580332544_group3_s_2_light | off |
| 衣柜 | 衣柜灯 灯 | light.lemesh_cn_2042902967_wy0d02_s_2_light | off |
| 主卧门外 | 主卧门外筒灯 灯 | light.090615_cn_2041100467_milg05_s_2_light | off |
| 浴室门外 | 浴室门外筒灯 灯 | light.090615_cn_2041206709_milg05_s_2_light | off |
| 浴室 | 浴霸 灯 | light.aupu_cn_965024497_s01md2_s_2_light | off |
| 浴室 | 浴室外筒灯 灯 | light.mijia_cn_group_1978088695174021121_group3_s_2_light | off |
| 厨房 | 平头熊F1调光筒射灯(Mesh2.0) 8 灯 | light.090615_cn_2020766823_milg05_s_2_light | on |
| 厨房 | 平头熊F1调光筒射灯(Mesh2.0) 5 灯 | light.090615_cn_2022075801_milg05_s_2_light | on |
| 厨房 | 平头熊F1调光筒射灯(Mesh2.0) 6 灯 | light.090615_cn_2022159375_milg05_s_2_light | on |
| 厨房 | 平头熊F1调光筒射灯(Mesh2.0) 7 灯 | light.090615_cn_2041206744_milg05_s_2_light | on |
| 厨房 | 油烟机 灯 | light.xiaomi_cn_2047692781_cyp10_s_6_light | off |
| 厨房 | 厨房筒灯 灯 | light.mijia_cn_group_1978090431347445760_group3_s_2_light | on |
| 鞋柜 | 鞋柜灯 灯 | light.lemesh_cn_2042893932_wy0d02_s_2_light | off |
| 玄关 | 玄关筒灯 灯 | light.mijia_cn_group_1978089679472308224_group3_s_2_light | off |

## Indicator Lights

| Area | Name | Entity | State |
| --- | --- | --- | --- |
| 客厅 | Xiaomi 中枢网关 指示灯 | light.xiaomi_cn_1179553687_hub1_s_3_indicator_light | on |
| 餐厨 | 餐厨开关（三键） 指示灯 | light.linp_cn_2002626186_t2dbw3_s_8_indicator_light | on |
| 走廊 | 左键-走廊开关 指示灯 | light.linp_cn_2002874216_t2dbw3_s_8_indicator_light | on |
| 阳台 | 阳台开关 指示灯 | light.linp_cn_2021957403_t2dbw2_s_8_indicator_light | on |
| 客厅 | 智能插座 指示灯 | light.cuco_cn_482606571_cp1_s_3_indicator_light | on |
| 主卧 | 主卧开关（双键） 指示灯 | light.linp_cn_2022408943_t2dbw2_s_8_indicator_light | off |
| 主卧 | 主卧空调 指示灯 | light.xiaomi_cn_862194962_m28_s_6_indicator_light | on |
| 书房 | 书房空调 指示灯 | light.xiaomi_cn_2007224174_r10h00_s_6_indicator_light | on |
| 书房 | 书房开关（双键） 指示灯 | light.linp_cn_2022388066_t2dbw2_s_8_indicator_light | on |
| 浴室 | 浴室开关（双键） 指示灯 | light.linp_cn_2022466912_t2dbw2_s_8_indicator_light | on |
| 玄关 | 玄关右 指示灯 | light.linp_cn_2022822455_t2dbw2_s_8_indicator_light | on |
| 玄关 | 玄关左 指示灯 | light.linp_cn_2043319688_t2dbw2_s_8_indicator_light | on |

## Noisiest Devices By Entity Count

| Device | Area | Total | Recommendation Mix |
| --- | --- | --- | --- |
| 逍遥002 Max（超薄基站版） | 浴室 | 218 | hide_or_disable_aux:121, keep_sensor_review:58, review:38, keep_primary:1 |
| 主卧空调 | 主卧 | 114 | keep_sensor_review:35, hide_or_disable_aux:66, review:10, keep_primary:2, keep_but_label_indicator:1 |
| 书房空调 | 书房 | 88 | keep_sensor_review:30, hide_or_disable_aux:49, review:7, keep_primary:1, keep_but_label_indicator:1 |
| 油烟机 | 厨房 | 72 | keep_sensor_review:23, review:12, hide_or_disable_aux:36, keep_primary:1 |
| 小米智能门锁 M30 人脸识别版 | 玄关 | 67 | hide_or_disable_aux:49, keep_sensor_review:9, review:9 |
| 衣柜灯 | 衣柜 | 51 | hide_or_disable_aux:50, keep_primary:1 |
| 鞋柜灯 | 鞋柜 | 51 | hide_or_disable_aux:50, keep_primary:1 |
| 浴室镜灯 | 浴室 | 44 | wrap_as_light:1, hide_or_disable_aux:43 |
| 平头熊F1调光筒射灯(Mesh2.0) 4 | 客厅 | 40 | hide_or_disable_aux:39, keep_primary:1 |
| 平头熊F1调光筒射灯(Mesh2.0) 3 | 客厅 | 40 | hide_or_disable_aux:39, keep_primary:1 |
| 平头熊F1调光筒射灯(Mesh2.0) 2 | 客厅 | 40 | hide_or_disable_aux:39, keep_primary:1 |
| 平头熊F1调光筒射灯(Mesh2.0) | 客厅 | 40 | hide_or_disable_aux:39, keep_primary:1 |
| 主卧门外筒灯 | 主卧门外 | 40 | hide_or_disable_aux:39, keep_primary:1 |
| 浴室门外筒灯 | 浴室门外 | 40 | hide_or_disable_aux:39, keep_primary:1 |
| 平头熊F1调光筒射灯(Mesh2.0) 8 | 厨房 | 40 | hide_or_disable_aux:39, keep_primary:1 |
| 平头熊F1调光筒射灯(Mesh2.0) 5 | 厨房 | 40 | hide_or_disable_aux:39, keep_primary:1 |
| 平头熊F1调光筒射灯(Mesh2.0) 6 | 厨房 | 40 | hide_or_disable_aux:39, keep_primary:1 |
| 平头熊F1调光筒射灯(Mesh2.0) 7 | 厨房 | 40 | hide_or_disable_aux:39, keep_primary:1 |
| 小饭煲 | 厨房 | 39 | hide_or_disable_aux:26, keep_sensor_review:13 |
| 餐厨开关（三键） | 餐厨 | 36 | hide_or_disable_aux:32, wrap_as_light:3, keep_but_label_indicator:1 |
| 左键-走廊开关 | 走廊 | 36 | hide_or_disable_aux:32, review:1, wrap_as_light:2, keep_but_label_indicator:1 |
| 阳台开关 | 阳台 | 30 | hide_or_disable_aux:27, wrap_as_light:1, review:1, keep_but_label_indicator:1 |
| 主卧开关（双键） | 主卧 | 30 | hide_or_disable_aux:27, wrap_as_light:2, keep_but_label_indicator:1 |
| 书房开关（双键） | 书房 | 30 | hide_or_disable_aux:27, wrap_as_light:1, review:1, keep_but_label_indicator:1 |
| 浴室开关（双键） | 浴室 | 30 | hide_or_disable_aux:27, review:2, keep_but_label_indicator:1 |
| 玄关右 | 玄关 | 30 | hide_or_disable_aux:27, review:2, keep_but_label_indicator:1 |
| 玄关左 | 玄关 | 30 | hide_or_disable_aux:27, review:2, keep_but_label_indicator:1 |
| 电视墙射灯 | 电视墙 | 10 | hide_or_disable_aux:9, keep_primary:1 |
| 浴室外筒灯 | 浴室 | 10 | hide_or_disable_aux:9, keep_primary:1 |
| 厨房筒灯 | 厨房 | 10 | hide_or_disable_aux:9, keep_primary:1 |

## Hide Or Disable Auxiliary Entity Candidates

There are 1159 auxiliary candidates. First 200 are listed below; full machine-readable list is in entity_audit.json.

| Domain | Name | Entity | Reason |
| --- | --- | --- | --- |
| sensor | Sun 下个清晨 | sensor.sun_next_dawn | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | Sun 下个黄昏 | sensor.sun_next_dusk | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | Sun 下个午夜 | sensor.sun_next_midnight | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | Sun 下个正午 | sensor.sun_next_noon | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | Sun 下次日出 | sensor.sun_next_rising | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | Sun 下次日落 | sensor.sun_next_setting | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| update | HACS update | update.hacs_update | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| update | Xiaomi Home update | update.xiaomi_home_update | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | Xiaomi 中枢网关 虚拟服务 产生虚拟事件 | notify.xiaomi_cn_1179553687_hub1_emit_virtual_event_a_4_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 餐厨开关（三键） * 自定义属性 互控ID&数量 | notify.linp_cn_2002626186_t2dbw3_get_local_ctrl_a_10_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 餐厨开关（三键） * 自定义属性 学习上报 | notify.linp_cn_2002626186_t2dbw3_enter_study_a_10_2 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 餐厨开关（三键） * 自定义属性 清除配对 | notify.linp_cn_2002626186_t2dbw3_clear_wireless_a_10_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 餐厨开关（三键） * 自定义属性 清除互控 | notify.linp_cn_2002626186_t2dbw3_clear_local_ctrl_a_10_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 餐厨开关（三键） * 自定义属性 获取单击 | notify.linp_cn_2002626186_t2dbw3_get_s_key_a_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 餐厨开关（三键） * 自定义属性 获取双击 | notify.linp_cn_2002626186_t2dbw3_get_d_key_a_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 餐厨开关（三键） * 自定义属性 获取长按 | notify.linp_cn_2002626186_t2dbw3_get_l_key_a_10_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 餐厨开关（三键） * 自定义属性 按键私有协议配置 | notify.linp_cn_2002626186_t2dbw3_set_key_a_10_8 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 餐厨开关（三键） * 自定义属性 设置通道橙灯亮 | notify.linp_cn_2002626186_t2dbw3_set_led_o_on_a_10_9 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 餐厨开关（三键） * 自定义属性 设置通道白灯亮 | notify.linp_cn_2002626186_t2dbw3_set_led_b_on_a_10_10 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 餐厨开关（三键） * 自定义属性 设置通道灯灭 | notify.linp_cn_2002626186_t2dbw3_set_led_off_a_10_11 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 左键-走廊开关 * 自定义属性 互控ID&数量 | notify.linp_cn_2002874216_t2dbw3_get_local_ctrl_a_10_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 左键-走廊开关 * 自定义属性 学习上报 | notify.linp_cn_2002874216_t2dbw3_enter_study_a_10_2 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 左键-走廊开关 * 自定义属性 清除配对 | notify.linp_cn_2002874216_t2dbw3_clear_wireless_a_10_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 左键-走廊开关 * 自定义属性 清除互控 | notify.linp_cn_2002874216_t2dbw3_clear_local_ctrl_a_10_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 左键-走廊开关 * 自定义属性 获取单击 | notify.linp_cn_2002874216_t2dbw3_get_s_key_a_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 左键-走廊开关 * 自定义属性 获取双击 | notify.linp_cn_2002874216_t2dbw3_get_d_key_a_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 左键-走廊开关 * 自定义属性 获取长按 | notify.linp_cn_2002874216_t2dbw3_get_l_key_a_10_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 左键-走廊开关 * 自定义属性 按键私有协议配置 | notify.linp_cn_2002874216_t2dbw3_set_key_a_10_8 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 左键-走廊开关 * 自定义属性 设置通道橙灯亮 | notify.linp_cn_2002874216_t2dbw3_set_led_o_on_a_10_9 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 左键-走廊开关 * 自定义属性 设置通道白灯亮 | notify.linp_cn_2002874216_t2dbw3_set_led_b_on_a_10_10 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 左键-走廊开关 * 自定义属性 设置通道灯灭 | notify.linp_cn_2002874216_t2dbw3_set_led_off_a_10_11 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 阳台开关 * 自定义属性 互控ID&数量 | notify.linp_cn_2021957403_t2dbw2_get_local_ctrl_a_10_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 阳台开关 * 自定义属性 学习上报 | notify.linp_cn_2021957403_t2dbw2_enter_study_a_10_2 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 阳台开关 * 自定义属性 清除配对 | notify.linp_cn_2021957403_t2dbw2_clear_wireless_a_10_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 阳台开关 * 自定义属性 清除互控 | notify.linp_cn_2021957403_t2dbw2_clear_local_ctrl_a_10_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 阳台开关 * 自定义属性 获取单击 | notify.linp_cn_2021957403_t2dbw2_get_s_key_a_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 阳台开关 * 自定义属性 获取双击 | notify.linp_cn_2021957403_t2dbw2_get_d_key_a_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 阳台开关 * 自定义属性 获取长按 | notify.linp_cn_2021957403_t2dbw2_get_l_key_a_10_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 阳台开关 * 自定义属性 按键私有协议配置 | notify.linp_cn_2021957403_t2dbw2_set_key_a_10_8 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 阳台开关 * 自定义属性 设置通道橙灯亮 | notify.linp_cn_2021957403_t2dbw2_set_led_o_on_a_10_9 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 阳台开关 * 自定义属性 设置通道蓝灯亮 | notify.linp_cn_2021957403_t2dbw2_set_led_b_on_a_10_10 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 阳台开关 * 自定义属性 设置通道灯灭 | notify.linp_cn_2021957403_t2dbw2_set_led_off_a_10_11 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 主卧开关（双键） * 自定义属性 互控ID&数量 | notify.linp_cn_2022408943_t2dbw2_get_local_ctrl_a_10_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 主卧开关（双键） * 自定义属性 学习上报 | notify.linp_cn_2022408943_t2dbw2_enter_study_a_10_2 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 主卧开关（双键） * 自定义属性 清除配对 | notify.linp_cn_2022408943_t2dbw2_clear_wireless_a_10_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 主卧开关（双键） * 自定义属性 清除互控 | notify.linp_cn_2022408943_t2dbw2_clear_local_ctrl_a_10_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 主卧开关（双键） * 自定义属性 获取单击 | notify.linp_cn_2022408943_t2dbw2_get_s_key_a_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 主卧开关（双键） * 自定义属性 获取双击 | notify.linp_cn_2022408943_t2dbw2_get_d_key_a_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 主卧开关（双键） * 自定义属性 获取长按 | notify.linp_cn_2022408943_t2dbw2_get_l_key_a_10_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 主卧开关（双键） * 自定义属性 按键私有协议配置 | notify.linp_cn_2022408943_t2dbw2_set_key_a_10_8 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 主卧开关（双键） * 自定义属性 设置通道橙灯亮 | notify.linp_cn_2022408943_t2dbw2_set_led_o_on_a_10_9 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 主卧开关（双键） * 自定义属性 设置通道蓝灯亮 | notify.linp_cn_2022408943_t2dbw2_set_led_b_on_a_10_10 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 主卧开关（双键） * 自定义属性 设置通道灯灭 | notify.linp_cn_2022408943_t2dbw2_set_led_off_a_10_11 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 衣柜灯 遥控器管理 删除遥控器1 | notify.lemesh_cn_2042902967_wy0d02_delete_remote_control_a_6_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用；包含安全敏感关键词，操作前必须确认 |
| notify | 衣柜灯 遥控器管理 删除遥控器2 | notify.lemesh_cn_2042902967_wy0d02_delete_remote_control_a_6_2 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用；包含安全敏感关键词，操作前必须确认 |
| notify | 衣柜灯 遥控器管理 删除遥控器3 | notify.lemesh_cn_2042902967_wy0d02_delete_remote_control_a_6_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用；包含安全敏感关键词，操作前必须确认 |
| notify | 衣柜灯 遥控器管理 删除遥控器4 | notify.lemesh_cn_2042902967_wy0d02_delete_remote_control_a_6_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用；包含安全敏感关键词，操作前必须确认 |
| notify | 书房开关（双键） * 自定义属性 互控ID&数量 | notify.linp_cn_2022388066_t2dbw2_get_local_ctrl_a_10_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 书房开关（双键） * 自定义属性 学习上报 | notify.linp_cn_2022388066_t2dbw2_enter_study_a_10_2 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 书房开关（双键） * 自定义属性 清除配对 | notify.linp_cn_2022388066_t2dbw2_clear_wireless_a_10_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 书房开关（双键） * 自定义属性 清除互控 | notify.linp_cn_2022388066_t2dbw2_clear_local_ctrl_a_10_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 书房开关（双键） * 自定义属性 获取单击 | notify.linp_cn_2022388066_t2dbw2_get_s_key_a_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 书房开关（双键） * 自定义属性 获取双击 | notify.linp_cn_2022388066_t2dbw2_get_d_key_a_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 书房开关（双键） * 自定义属性 获取长按 | notify.linp_cn_2022388066_t2dbw2_get_l_key_a_10_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 书房开关（双键） * 自定义属性 按键私有协议配置 | notify.linp_cn_2022388066_t2dbw2_set_key_a_10_8 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 书房开关（双键） * 自定义属性 设置通道橙灯亮 | notify.linp_cn_2022388066_t2dbw2_set_led_o_on_a_10_9 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 书房开关（双键） * 自定义属性 设置通道蓝灯亮 | notify.linp_cn_2022388066_t2dbw2_set_led_b_on_a_10_10 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 书房开关（双键） * 自定义属性 设置通道灯灭 | notify.linp_cn_2022388066_t2dbw2_set_led_off_a_10_11 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 浴室开关（双键） * 自定义属性 互控ID&数量 | notify.linp_cn_2022466912_t2dbw2_get_local_ctrl_a_10_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 浴室开关（双键） * 自定义属性 学习上报 | notify.linp_cn_2022466912_t2dbw2_enter_study_a_10_2 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 浴室开关（双键） * 自定义属性 清除配对 | notify.linp_cn_2022466912_t2dbw2_clear_wireless_a_10_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 浴室开关（双键） * 自定义属性 清除互控 | notify.linp_cn_2022466912_t2dbw2_clear_local_ctrl_a_10_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 浴室开关（双键） * 自定义属性 获取单击 | notify.linp_cn_2022466912_t2dbw2_get_s_key_a_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 浴室开关（双键） * 自定义属性 获取双击 | notify.linp_cn_2022466912_t2dbw2_get_d_key_a_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 浴室开关（双键） * 自定义属性 获取长按 | notify.linp_cn_2022466912_t2dbw2_get_l_key_a_10_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 浴室开关（双键） * 自定义属性 按键私有协议配置 | notify.linp_cn_2022466912_t2dbw2_set_key_a_10_8 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 浴室开关（双键） * 自定义属性 设置通道橙灯亮 | notify.linp_cn_2022466912_t2dbw2_set_led_o_on_a_10_9 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 浴室开关（双键） * 自定义属性 设置通道蓝灯亮 | notify.linp_cn_2022466912_t2dbw2_set_led_b_on_a_10_10 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 浴室开关（双键） * 自定义属性 设置通道灯灭 | notify.linp_cn_2022466912_t2dbw2_set_led_off_a_10_11 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 获取区域信息 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_get_zone_configs_a_2_10 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 获取房间信息 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_get_room_configs_a_2_11 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 设置划区 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_set_zone_a_2_12 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 设置房间清扫参数 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_set_room_clean_configs_a_2_13 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 分割房间 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_split_room_a_2_14 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 合并房间 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_merge_rooms_a_2_15 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 开始选区清扫 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_start_vacuum_room_sweep_a_2_16 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 新增预约清扫 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_add_order_clean_a_2_23 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 修改预约清扫 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_modify_order_clean_a_2_24 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 删除预约清扫 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_delete_order_clean_a_2_25 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用；包含安全敏感关键词，操作前必须确认 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 开始划区清扫 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_start_zone_sweep_a_2_37 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 添加自定义清扫 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_add_user_sweep_setting_a_2_38 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 删除自定义清扫 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_del_user_sweep_setting_a_2_39 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用；包含安全敏感关键词，操作前必须确认 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 修改自定义清扫 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_modify_user_sweep_setting_a_2_40 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 设置自定义 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_user_define_sweep_set_a_2_41 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 开始自定义清扫清扫 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_start_user_define_sweep_a_2_42 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 设置地图房间名称 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_set_room_name_a_2_47 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 打扫房间 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_start_room_sweep_a_2_48 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 最后清扫 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_final_cleaning_a_2_54 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 跳过清扫 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_skip_cleaning_a_2_55 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 临时加扫房间 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_temporary_cleaning_room_a_2_56 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 扫地机 临时加扫区域 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_temporary_cleaning_zone_a_2_57 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 语音管理 下载语音包 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_download_voice_a_12_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 逍遥002 Max（超薄基站版） 语音管理 获取下载状态 | notify.narwa_cn_x_12053_1479518829_bywbpqsxec_ded8caa5f3b24d43ad6519a8fa95ae16_cx7_get_download_status_a_12_2 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 小饭煲 电饭煲 开始烹饪 | notify.chunmi_cn_583160283_eh3_start_cook_a_2_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 小饭煲 * 自定义 开始烹饪 | notify.chunmi_cn_583160283_eh3_cooking_start_a_3_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 小饭煲 * 自定义 设置食谱 | notify.chunmi_cn_583160283_eh3_set_menu_a_3_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 小饭煲 * 自定义 设置设备参数 | notify.chunmi_cn_583160283_eh3_set_setting_a_3_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 小饭煲 * 自定义 获取日志数据； log-index为0时返回的数据表示一共有多少个错误记录，无错误数据记录时返回“No Error"；非0时的数N时，数据将返回最后N*50个错误记录。 每个错误记录的格式tttt--ssssaaaaaaaabbcc： tttt：10进制字符，表示返回错误记录的数量； ssss：10进制字符，表示序号，从0001开始； aaaaaaaa：16进制字符，表示时间戳； bb：16进制字符，表示错误代码； cc：16进制字符表示错误信息。 | notify.chunmi_cn_583160283_eh3_get_log_data_a_3_8 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 小饭煲 * 自定义 获取自检故障数据 | notify.chunmi_cn_583160283_eh3_get_selfcheck_a_3_10 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 小米智能门锁 M30 人脸识别版 * 门锁设置自定义wifi服务 下发数据到门锁 | notify.xiaomi_cn_1154312776_m30fc_send_data_a_11_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用；包含安全敏感关键词，操作前必须确认 |
| notify | 玄关右 * 自定义属性 互控ID&数量 | notify.linp_cn_2022822455_t2dbw2_get_local_ctrl_a_10_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关右 * 自定义属性 学习上报 | notify.linp_cn_2022822455_t2dbw2_enter_study_a_10_2 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关右 * 自定义属性 清除配对 | notify.linp_cn_2022822455_t2dbw2_clear_wireless_a_10_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关右 * 自定义属性 清除互控 | notify.linp_cn_2022822455_t2dbw2_clear_local_ctrl_a_10_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关右 * 自定义属性 获取单击 | notify.linp_cn_2022822455_t2dbw2_get_s_key_a_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关右 * 自定义属性 获取双击 | notify.linp_cn_2022822455_t2dbw2_get_d_key_a_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关右 * 自定义属性 获取长按 | notify.linp_cn_2022822455_t2dbw2_get_l_key_a_10_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关右 * 自定义属性 按键私有协议配置 | notify.linp_cn_2022822455_t2dbw2_set_key_a_10_8 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关右 * 自定义属性 设置通道橙灯亮 | notify.linp_cn_2022822455_t2dbw2_set_led_o_on_a_10_9 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关右 * 自定义属性 设置通道蓝灯亮 | notify.linp_cn_2022822455_t2dbw2_set_led_b_on_a_10_10 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关右 * 自定义属性 设置通道灯灭 | notify.linp_cn_2022822455_t2dbw2_set_led_off_a_10_11 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 鞋柜灯 遥控器管理 删除遥控器1 | notify.lemesh_cn_2042893932_wy0d02_delete_remote_control_a_6_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用；包含安全敏感关键词，操作前必须确认 |
| notify | 鞋柜灯 遥控器管理 删除遥控器2 | notify.lemesh_cn_2042893932_wy0d02_delete_remote_control_a_6_2 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用；包含安全敏感关键词，操作前必须确认 |
| notify | 鞋柜灯 遥控器管理 删除遥控器3 | notify.lemesh_cn_2042893932_wy0d02_delete_remote_control_a_6_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用；包含安全敏感关键词，操作前必须确认 |
| notify | 鞋柜灯 遥控器管理 删除遥控器4 | notify.lemesh_cn_2042893932_wy0d02_delete_remote_control_a_6_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用；包含安全敏感关键词，操作前必须确认 |
| notify | 玄关左 * 自定义属性 互控ID&数量 | notify.linp_cn_2043319688_t2dbw2_get_local_ctrl_a_10_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关左 * 自定义属性 学习上报 | notify.linp_cn_2043319688_t2dbw2_enter_study_a_10_2 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关左 * 自定义属性 清除配对 | notify.linp_cn_2043319688_t2dbw2_clear_wireless_a_10_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关左 * 自定义属性 清除互控 | notify.linp_cn_2043319688_t2dbw2_clear_local_ctrl_a_10_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关左 * 自定义属性 获取单击 | notify.linp_cn_2043319688_t2dbw2_get_s_key_a_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关左 * 自定义属性 获取双击 | notify.linp_cn_2043319688_t2dbw2_get_d_key_a_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关左 * 自定义属性 获取长按 | notify.linp_cn_2043319688_t2dbw2_get_l_key_a_10_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关左 * 自定义属性 按键私有协议配置 | notify.linp_cn_2043319688_t2dbw2_set_key_a_10_8 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关左 * 自定义属性 设置通道橙灯亮 | notify.linp_cn_2043319688_t2dbw2_set_led_o_on_a_10_9 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关左 * 自定义属性 设置通道蓝灯亮 | notify.linp_cn_2043319688_t2dbw2_set_led_b_on_a_10_10 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| notify | 玄关左 * 自定义属性 设置通道灯灭 | notify.linp_cn_2043319688_t2dbw2_set_led_off_a_10_11 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 餐厨开关（三键） * 自定义属性 本地互控 | sensor.linp_cn_2002626186_t2dbw3_local_control_p_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 餐厨开关（三键） * 自定义属性 本地控制 | sensor.linp_cn_2002626186_t2dbw3_key_param_p_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 左键-走廊开关 * 自定义属性 本地互控 | sensor.linp_cn_2002874216_t2dbw3_local_control_p_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 左键-走廊开关 * 自定义属性 本地控制 | sensor.linp_cn_2002874216_t2dbw3_key_param_p_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 阳台开关 * 自定义属性 本地互控 | sensor.linp_cn_2021957403_t2dbw2_local_control_p_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 阳台开关 * 自定义属性 本地控制 | sensor.linp_cn_2021957403_t2dbw2_key_param_p_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 主卧开关（双键） * 自定义属性 本地互控 | sensor.linp_cn_2022408943_t2dbw2_local_control_p_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 主卧开关（双键） * 自定义属性 本地控制 | sensor.linp_cn_2022408943_t2dbw2_key_param_p_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 衣柜灯 遥控器管理 遥控器列表1 | sensor.lemesh_cn_2042902967_wy0d02_remote_control_list_p_6_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 衣柜灯 遥控器管理 遥控器列表2 | sensor.lemesh_cn_2042902967_wy0d02_remote_control_list_p_6_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 衣柜灯 遥控器管理 遥控器列表3 | sensor.lemesh_cn_2042902967_wy0d02_remote_control_list_p_6_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 衣柜灯 遥控器管理 遥控器列表4 | sensor.lemesh_cn_2042902967_wy0d02_remote_control_list_p_6_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 主卧空调 * 增强 根据温度等返回可调节的湿度范围 | sensor.xiaomi_cn_862194962_m28_humidity_range_p_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 书房空调 * 增强 根据温度等返回可调节的湿度范围 | sensor.xiaomi_cn_2007224174_r10h00_humidity_range_p_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 书房空调 * 增强 温湿度传感器中的温度 | sensor.xiaomi_cn_2007224174_r10h00_tp_and_humidity_p_10_9 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 书房开关（双键） * 自定义属性 本地互控 | sensor.linp_cn_2022388066_t2dbw2_local_control_p_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 书房开关（双键） * 自定义属性 本地控制 | sensor.linp_cn_2022388066_t2dbw2_key_param_p_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 浴室开关（双键） * 自定义属性 本地互控 | sensor.linp_cn_2022466912_t2dbw2_local_control_p_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 浴室开关（双键） * 自定义属性 本地控制 | sensor.linp_cn_2022466912_t2dbw2_key_param_p_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 玄关右 * 自定义属性 本地互控 | sensor.linp_cn_2022822455_t2dbw2_local_control_p_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 玄关右 * 自定义属性 本地控制 | sensor.linp_cn_2022822455_t2dbw2_key_param_p_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 鞋柜灯 遥控器管理 遥控器列表1 | sensor.lemesh_cn_2042893932_wy0d02_remote_control_list_p_6_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 鞋柜灯 遥控器管理 遥控器列表2 | sensor.lemesh_cn_2042893932_wy0d02_remote_control_list_p_6_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 鞋柜灯 遥控器管理 遥控器列表3 | sensor.lemesh_cn_2042893932_wy0d02_remote_control_list_p_6_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 鞋柜灯 遥控器管理 遥控器列表4 | sensor.lemesh_cn_2042893932_wy0d02_remote_control_list_p_6_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 玄关左 * 自定义属性 本地互控 | sensor.linp_cn_2043319688_t2dbw2_local_control_p_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| sensor | 玄关左 * 自定义属性 本地控制 | sensor.linp_cn_2043319688_t2dbw2_key_param_p_10_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 4 灯 凌动开关 | switch.090615_cn_2022122260_milg05_flex_switch_p_2_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 4 灯 关闭上电色温切换 | switch.090615_cn_2022122260_milg05_flow_p_2_12 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 4 * 设置模式 节律自动运行 | switch.090615_cn_2022122260_milg05_rhythmauto_p_4_25 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 4 * 设置模式 夜灯开关使能 | switch.090615_cn_2022122260_milg05_nightonoff_p_4_26 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 4 * 设置模式 单色温模式使能 | switch.090615_cn_2022122260_milg05_singlecw_p_4_29 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 3 灯 凌动开关 | switch.090615_cn_2041348683_milg05_flex_switch_p_2_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 3 灯 关闭上电色温切换 | switch.090615_cn_2041348683_milg05_flow_p_2_12 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 3 * 设置模式 节律自动运行 | switch.090615_cn_2041348683_milg05_rhythmauto_p_4_25 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 3 * 设置模式 夜灯开关使能 | switch.090615_cn_2041348683_milg05_nightonoff_p_4_26 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 3 * 设置模式 单色温模式使能 | switch.090615_cn_2041348683_milg05_singlecw_p_4_29 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 阳台帘 窗帘电机 电机反向 | switch.bjkcz_cn_2096576206_kczble_motor_reverse_p_2_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 2 灯 凌动开关 | switch.090615_cn_947717173_milg05_flex_switch_p_2_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 2 灯 关闭上电色温切换 | switch.090615_cn_947717173_milg05_flow_p_2_12 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 2 * 设置模式 节律自动运行 | switch.090615_cn_947717173_milg05_rhythmauto_p_4_25 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 2 * 设置模式 夜灯开关使能 | switch.090615_cn_947717173_milg05_nightonoff_p_4_26 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 2 * 设置模式 单色温模式使能 | switch.090615_cn_947717173_milg05_singlecw_p_4_29 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 灯 凌动开关 | switch.090615_cn_947770195_milg05_flex_switch_p_2_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) 灯 关闭上电色温切换 | switch.090615_cn_947770195_milg05_flow_p_2_12 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) * 设置模式 节律自动运行 | switch.090615_cn_947770195_milg05_rhythmauto_p_4_25 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) * 设置模式 夜灯开关使能 | switch.090615_cn_947770195_milg05_nightonoff_p_4_26 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 平头熊F1调光筒射灯(Mesh2.0) * 设置模式 单色温模式使能 | switch.090615_cn_947770195_milg05_singlecw_p_4_29 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 衣柜灯 灯 凌动开关 | switch.lemesh_cn_2042902967_wy0d02_flex_switch_p_2_12 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 衣柜灯 灯 夜灯开关 | switch.lemesh_cn_2042902967_wy0d02_night_light_switch_p_2_13 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 衣柜灯 遥控器管理 遥控器添加开关 | switch.lemesh_cn_2042902967_wy0d02_remote_control_addable_p_6_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 衣柜灯 遥控器管理 遥控器禁止添加开关 | switch.lemesh_cn_2042902967_wy0d02_remote_control_addable_p_6_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 衣柜灯 * 默认状态 主从灯开关 | switch.lemesh_cn_2042902967_wy0d02_master_slave_switch_p_5_19 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 主卧窗帘 窗帘电机 电机反向 | switch.bjkcz_cn_2098420438_kczble_motor_reverse_p_2_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 主卧空调 提示音 提示音 | switch.xiaomi_cn_862194962_m28_alarm_p_5_1 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 主卧空调 空调开发者模式 缓解导风板凝水 | switch.xiaomi_cn_862194962_m28_relieve_air_deflector_condensation_p_25_3 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 主卧空调 空调开发者模式 制冷室外风扇降噪 | switch.xiaomi_cn_862194962_m28_cooling_outdoor_fan_noise_reduction_p_25_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 主卧空调 空调开发者模式 制冷室内风扇降噪 | switch.xiaomi_cn_862194962_m28_cooling_indoor_fan_noise_reduction_p_25_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 主卧空调 空调开发者模式 制热室外风扇降噪 | switch.xiaomi_cn_862194962_m28_heating_outdoor_fan_noise_reduction_p_25_6 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 主卧空调 空调开发者模式 制热室内风扇降噪 | switch.xiaomi_cn_862194962_m28_heating_indoor_fan_noise_reduction_p_25_7 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 主卧空调 空调开发者模式 制热达温停机改善开关 | switch.xiaomi_cn_862194962_m28_improve_heat_tar_temp_stop_p_25_9 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 主卧空调 * 增强 diy睡眠 | switch.xiaomi_cn_862194962_m28_sleep_diy_p_10_4 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 主卧空调 * 增强 左右摆风中第二个摆风分区 | switch.xiaomi_cn_862194962_m28_secondpart_of_hswing_p_10_5 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |
| switch | 主卧空调 * 增强 关机下不执行标志位 | switch.xiaomi_cn_862194962_m28_off_flag_p_10_8 | 高级参数/事件/按钮/私有属性，建议隐藏或禁用 |

## Suggested Next Actions

1. Review switches listed under “Switches That Should Probably Become Lights”.
2. Add approved wrappers from suggested_template_lights.yaml to HA configuration or create equivalent helpers in UI.
3. Hide auxiliary entities from dashboards and voice/conversation exposure first; disable only after confirming no automations rely on them.
4. Keep home_semantics.yaml updated as Jarvis' source of truth for household meaning.
