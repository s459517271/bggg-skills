# 环境与授权准备

## 飞书 CLI

先检查，不要假设用户已经安装：

```bash
command -v lark-cli
lark-cli --version
```

未安装时，先告知用户将安装官方 `@larksuite/cli`，取得同意后执行：

```bash
npm install -g @larksuite/cli
```

该 CLI 需要 Node.js 16 或更高版本。安装后依次完成：

1. `lark-cli config init --new`：按提示配置飞书应用。
2. 按 `lark-shared` 的 split-flow 发起用户授权；优先根据实际命令缺少的 scope 做最小权限授权，不要擅自输出或保存密钥。
3. `lark-cli auth status --json --verify`：确认 user 身份有效。
4. 用一个只读 Base 命令验证访问；权限不足时按错误中的 `hint`和`permission_violations`补授权。

已经安装时不要重复安装。版本提示不应打断当前任务；只有兼容性故障或用户要求时才更新。

## 浏览器

确认 Codex 能通过 `chrome:control-chrome`连接用户指定的 Chrome，并且该浏览器已登录可用的 Gemini/Flow 账号。不要读取 cookies、密码、配置文件或浏览器存储。

为每个账号记录用户提供的`账号别名＋Chrome配置显示名称＋允许入口`。若有多个账号，再确认启用状态、优先级、是否允许自动切换和账号粘性；完整登记与轮询规则见 [account-routing.md](account-routing.md)。

若用户有多个 Chrome 配置，只记录用户选择的显示名称；不要把某台机器上的 profile 路径写进 Skill 或 Base。切换后必须从页面可见身份核对当前账号，不能只凭窗口顺序或上次记忆判断。

## 本地目录

每次新会话确认：

- 工作目录：下载素材、抽帧、九宫格、尾帧和临时验收帧。
- 成品目录：原始带水印视频、消除水印版和最终确认版。

所有路径都来自当前用户，不在 Skill 中内置用户名、桌面目录或绝对路径。

## 去水印能力

检查当前 Skills 是否存在`gemini-watermark-remover`。缺失时按 [postprocess-sop.md](postprocess-sop.md) 说明来源和安装动作，取得用户同意后安装；不能把`delogo`、模糊、马赛克、遮挡或裁边当成替代方案。

## 视频工具

检查`ffmpeg`和`ffprobe`。缺失时先说明它们用于读取视频规格、抽帧、抽真实尾帧和验收音视频轨，并取得用户同意后按当前操作系统安装。安装后分别运行版本命令验证，不能只检查安装器返回值。
