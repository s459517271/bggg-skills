# 生图后端选择与 API 兜底

## 1. 内置生图能力优先

如果当前 Codex、ChatGPT 或 Agent 工具列表中存在 `image_gen` 或等效图片生成能力：

- 直接使用内置能力。
- 把已确认的产品主控图作为参考图传入。
- 使用已经确认的提示词、尺寸意图和文件名。
- 生成后把结果保存或复制到规划目录，并按命名规范重命名。
- 不检查、索取或配置 API Key。

## 2. 何时启用 API 脚本

只有当前运行环境完全没有可调用的图片生成工具时，才使用：

```text
scripts/generate_image.py
```

默认实现使用 OpenAI Images API。其他提供商只有在兼容 OpenAI Images API 时，才可以通过 `OPENAI_BASE_URL` 和 `IMAGE_MODEL` 切换；不兼容的接口需要另写适配器，不能假装已经支持。

## 3. 环境变量

```bash
export OPENAI_API_KEY="..."
export IMAGE_MODEL="gpt-image-1"          # 可选
export OPENAI_BASE_URL="https://.../v1"  # 可选，仅兼容端点需要
```

不要把真实密钥写入命令历史示例、Skill 文件、日志或最终回复。用户未配置密钥时，只说明缺少哪个环境变量。

## 4. 安装 API 兜底依赖

仅在需要 API 兜底的环境安装：

```bash
python3 -m pip install -r "scripts/requirements-image-api.txt"
```

拥有内置生图能力时不要为了“验证”而安装这些依赖。

## 5. 调用示例

纯文本生图：

```bash
python3 "scripts/generate_image.py" \
  --prompt-file "/path/to/confirmed-prompt.txt" \
  --output "/path/to/2026-08-06_pet-supplies_product_01-white-background_full-kit_v01.png"
```

带产品参考图：

```bash
python3 "scripts/generate_image.py" \
  --prompt-file "/path/to/confirmed-prompt.txt" \
  --reference "/path/to/product-front.png" \
  --reference "/path/to/product-side.png" \
  --output "/path/to/2026-08-06_pet-supplies_product_02-showcase_front-45-degree_v01.png"
```

## 6. 脚本边界

- 每次只生成 1 张，整套仍逐张调用。
- 输出文件已存在时停止，禁止覆盖。
- `--reference` 可重复传入多张产品图；有参考图时使用图片编辑接口，没有时使用图片生成接口。
- 默认 API 生成尺寸为 `1024x1024`，随后高质量调整到规划的 `2000x2000`。这只是满足交付像素，不等于增加原生细节；质检时仍要检查清晰度。
- API 返回 URL 或 base64 图片都可保存。
- 脚本不会把提示词、参考图或密钥上传到用户未指定的其他服务。

