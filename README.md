# bggg-skills

Open-source Codex skills from BGGG.

This repository is organized as a skill collection. Each skill lives in its own top-level folder and can be copied or symlinked into `~/.codex/skills/`.

## Skills

- [`bggg-creator-image2psd`](./bggg-creator-image2psd): turn one or more images into layered PSD files, with Codex/imagegen-assisted workflows, full-canvas PNG layer export, and a pure-Python PSD writer.

## Install A Skill

Clone this repository:

```bash
git clone https://github.com/binggandata/bggg-skills.git
cd bggg-skills
```

Copy a skill into Codex:

```bash
mkdir -p ~/.codex/skills
cp -R bggg-creator-image2psd ~/.codex/skills/
```

Or symlink it while developing:

```bash
ln -s "$PWD/bggg-creator-image2psd" ~/.codex/skills/bggg-creator-image2psd
```

Then install that skill's dependencies if it has a `scripts/requirements.txt`.

## License

MIT
