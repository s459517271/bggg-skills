# 输出目录与命名规范

## 默认输出目录

用户未指定保存位置时，以 Skill 根目录为基准创建：

```text
outputs/{YYYY-MM-DD}_{category-slug}_{product-slug}/
```

示例：

```text
outputs/2026-08-06_pet-supplies_dog-water-bottle/
```

目录中的 `category-slug` 和 `product-slug` 使用简短、可读的小写英文，单词以连字符连接。用户只给中文时，根据业务卡生成英文 slug，并在生图规划中展示给用户确认。

## 套图子文件夹分类

同一产品的多张图片不得全部混放在产品根目录，必须按图片类型建子文件夹分类存放：

```text
outputs/{YYYY-MM-DD}_{category-slug}_{product-slug}/
  01-产品主图/
  02-展示图/
  03-卖点图/
  04-英雄图/
  05-细节图/
  06-场景图/
```

- 只创建本轮实际生成的类型文件夹，不建空文件夹。
- 文件命名规则不变，版本记录（`vNN`、`vNN-final`、`vNN-superseded`）随文件一起进入对应子文件夹。
- 用户指定其他分类方式时以用户为准。

## 类型固定编码

| 编码 | 图片类型 | type slug |
| --- | --- | --- |
| 01 | 白底图 | `white-background` |
| 02 | 展示图 | `showcase` |
| 03 | 卖点图 | `selling-point` |
| 04 | 英雄图 | `hero` |
| 05 | 细节图 | `detail` |
| 06 | 场景图 | `lifestyle` |

## 文件命名

```text
{YYYY-MM-DD}_{category-slug}_{product-slug}_{type-code}-{type-slug}_{focus-slug}_vNN.png
```

示例：

```text
2026-08-06_pet-supplies_dog-water-bottle_01-white-background_full-kit_v01.png
2026-08-06_pet-supplies_dog-water-bottle_02-showcase_front-45-degree_v01.png
2026-08-06_pet-supplies_dog-water-bottle_03-selling-point_leakproof-lock_v01.png
2026-08-06_pet-supplies_dog-water-bottle_04-hero_outdoor-adventure_v01.png
2026-08-06_pet-supplies_dog-water-bottle_05-detail_silicone-seal_v01.png
2026-08-06_pet-supplies_dog-water-bottle_06-lifestyle_hiking-use_v01.png
```

## 版本与最终稿

- 初次生成使用 `v01`。
- 每次返工递增为 `v02`、`v03`，禁止覆盖旧文件。
- 用户确认某个版本后，将确认文件复制为同名的 `vNN-final.png`；保留原版本作为过程记录。
- 同一类型生成多张时，在 `focus-slug` 中体现差异，例如 `front-45-degree`、`back-packaging`、`kitchen-use`。
- 不使用 `image1.png`、`final-final.png`、`新建文件.png` 等无法辨识内容的名称。

## 输出前确认

生图前必须向用户展示：

1. 输出目录绝对路径。
2. 本轮每张图片的完整文件名。
3. 当前版本号。

用户修改目录、品类或产品名后，重新计算全部文件名再确认。
