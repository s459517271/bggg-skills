# Gemini 视频去水印 SOP

## 工具职责

使用 `GargantuaX/gemini-watermark-remover` 处理 Gemini/Veo 可见星形水印。该工具使用水印模型恢复被 Alpha 合成改变的像素，并可清理残留；不是 `delogo`、模糊或马赛克。

仅处理用户拥有或获授权的视频。

## 开始前确认

复用主流程已经确认的输入文件和统一输出目录。若未提供，先确认：

1. 哪个原始视频需要处理。
2. 原始带水印文件、消除水印版和验收帧输出到哪里。

## Skill 检查与安装

1. 先检查当前可用 Skills 中是否已有`gemini-watermark-remover`。
2. 已有时，先读取该 Skill 的`SKILL.md`并确认它是否明确支持当前文件类型。Skill只声明图片时，不要假设它已经覆盖视频；视频改走本仓库的`bin/gwr.mjs`。
3. 没有时，告知用户将从`GargantuaX/gemini-watermark-remover`安装开源 Skill；取得同意后执行：

```bash
pnpm dlx skills add GargantuaX/gemini-watermark-remover --skill gemini-watermark-remover --yes
```

4. 安装后重新检查 Skill 是否可发现，并读取其完整说明。安装失败、Skill只支持图片或视频运行失败时，使用下方仓库本地构建作为视频兜底；不要静默改用模糊或遮盖方案。
5. 若`pnpm`不可用，先说明需要安装Node.js和pnpm并取得用户同意；不要擅自安装全局依赖。

## 消除 Gemini 可见水印

保留原始下载文件并在文件名标记`原始带水印`。仅在 Skill 安装不可用时安装并构建仓库：

```bash
git clone --depth 1 https://github.com/GargantuaX/gemini-watermark-remover.git
cd gemini-watermark-remover
pnpm install --frozen-lockfile
pnpm build
pnpm exec playwright install chromium
```

处理视频：

```bash
node bin/gwr.mjs remove input.mp4 \
  --output output-消除水印.mp4 \
  --overwrite \
  --json
```

若已安装的仓库 Skill 明确支持当前输入类型，可改用：

```bash
node skills/gemini-watermark-remover/scripts/run.mjs remove input.mp4 \
  --output output-消除水印.mp4
```

不要改用 `ffmpeg delogo`、高斯模糊、马赛克、贴图覆盖或裁边。工具因检测置信度、尺寸或导出失败而停止时，保留原片并记录失败，不得生成伪成品。

批量处理时逐条运行并验收。不要并发启动多个本地浏览器去水印任务；它们可能争用临时端口，出现命令结束但未产出文件的假成功。

## 文字钩子检查与补字

原作屏幕文字承担反转、悬念、身份、价格、结果或行动号召时，把它视为成品必要资产，不是可选装饰。

1. 从`爆款拆解`和视频提示词的`TEXT HOOK`读取精确原文、大小写、拼写、标点、换行、位置、样式和出现区间；不替原作者纠正语法。
2. 抽取成片开头、中间和结尾帧，检查文字是否存在且可读。Gemini/Flow 未生成、生成乱码或只短暂出现时，进入后期补字；已经正确存在时不得重复覆盖。
3. 优先使用当前环境已有的确定性字幕/图层能力。`ffmpeg`支持`drawtext`时可直接渲染；不支持时，先生成与视频同尺寸的透明PNG/SVG文字图层，再用`overlay`叠加。不要为补一句文字擅自安装新的全局依赖。
4. 匹配原作的相对位置、对齐、字号层级、颜色、描边/阴影、行距和持续时间；保证9:16安全区内可读，不遮挡产品核心信息。不要默认套用粗黑描边、花字或模板字体；原作是普通白字时就使用普通白色无衬线字，只保留原作可见的轻微阴影。
5. 补字后保留原音轨，再用`ffprobe`验证画幅、时长、视频轨和音频轨；分别抽取开头、中间和结尾帧确认没有缺字、错字、乱码、裁切、闪烁或重复叠字。
6. 文件名标记`补文字钩子`。在Base的`运行日志`和`最后成功步骤`记录检查结果、是否补字和最终文件；先上传并回读新版，再删除被替换的旧附件。

## 成品验收与回传

1. 分别抽取开头、中间和结尾帧，放大水印区域。
2. 确认星形标记和尖角完全消失，原背景纹理、边缘和运动连续，没有矩形模糊块、涂抹、闪烁或新噪点。
3. 原作存在必要文字钩子时，同时确认最终成片文字完整、准确、可读且时间范围正确。
4. 用 `ffprobe` 确认宽小于高、宽高比接近9:16、时长与原片基本一致、视频轨和音频轨都存在。
5. 多段续接从最终后处理文件抽取最后一个稳定帧。
6. 飞书成品字段只上传完成去水印、必要补字并通过验收的文件。替换旧附件前实时回读字段，避免重复追加或误删用户文件。
7. 替换附件采用“先上传新文件 → 回读文件名、token、大小 → 删除旧附件 → 再回读”的顺序；不得先删后传。
