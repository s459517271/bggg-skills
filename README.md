# bggg-skills

中文 | [English](./README_EN.md)

`bggg-skills` 是 BGGG 开源的 Codex Skills 集合仓库。

每个 skill 都是一个独立目录，可以复制或软链接到 `~/.codex/skills/` 使用。后续更多 BGGG 的可复用工作流、工具封装和创作能力都会逐步放到这个仓库里。

Created by [@binggandata](https://github.com/binggandata) · [小红书](https://xhslink.com/m/4ndptyfq4vu) · [X / Twitter](https://x.com/bggg_ai) · 微信：binggandata2

## 当前 Skills

- [`bggg-creator-image2psd`](./bggg-creator-image2psd)：把一张或多张图片转成可编辑的分层 PSD，支持 Codex/imagegen 辅助拆图、全画布 PNG 图层导出、颜色拆层、白底转透明，以及纯 Python PSD 写入。
- [`bggg-skill-taotie`](./bggg-skill-taotie)：Skill 进化器，通过对比、分析和吸收其他 skill 的优势，帮助目标 skill 渐进式升级。

## 安装

克隆仓库：

```bash
git clone https://github.com/binggandata/bggg-skills.git
cd bggg-skills
```

复制某个 skill 到 Codex：

```bash
mkdir -p ~/.codex/skills
cp -R bggg-creator-image2psd ~/.codex/skills/
```

开发时也可以用软链接：

```bash
ln -s "$PWD/bggg-creator-image2psd" ~/.codex/skills/bggg-creator-image2psd
```

如果 skill 目录下有 `scripts/requirements.txt`，再安装它的依赖：

```bash
python3 -m pip install -r ~/.codex/skills/bggg-creator-image2psd/scripts/requirements.txt
```

## 仓库结构

```text
bggg-skills/
├── README.md
├── README_EN.md
├── LICENSE
├── bggg-creator-image2psd/
│   ├── SKILL.md
│   ├── README.md
│   ├── README_EN.md
│   ├── scripts/
│   ├── references/
│   ├── assets/
│   ├── evals/
│   └── projects/
└── bggg-skill-taotie/
    ├── SKILL.md
    ├── README.md
    ├── INSTALL.md
    ├── references/
    └── evals/
```

`projects/` 是 skill 运行时的本地项目输出目录。开源仓库只保留 `.gitkeep`，不会提交实际生成的图片、PSD、zip 或过程文件。

## 贡献新 Skill

推荐每个 skill 使用下面的基本结构：

```text
skill-name/
├── SKILL.md
├── README.md
├── README_EN.md
├── scripts/
├── references/
├── assets/
├── evals/
└── projects/.gitkeep
```

其中：

- `SKILL.md` 给 Codex 读取，用于触发和执行。
- `README.md` 是中文主说明，给用户阅读。
- `README_EN.md` 是英文说明。
- `scripts/` 放确定性脚本。
- `references/` 放按需读取的参考材料。
- `projects/` 放运行产物，默认不提交。

## License

MIT
