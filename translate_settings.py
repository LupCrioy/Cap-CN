import os

settings_dir = "D:/HANA-WORKSPACE/KFZ-WORKSPACE/Cap-CN/apps/desktop/src/routes/(window-chrome)/settings"

translations = {
    # changelog.tsx
    "Failed to fetch changelog": "获取更新日志失败",

    # cli.tsx
    "Cap CLI installed": "Cap CLI 已安装",
    "Cap CLI removed": "Cap CLI 已移除",
    "Command Line": "命令行",
    "Copied to clipboard": "已复制到剪贴板",
    "Failed to install CLI": "安装 CLI 失败",
    "Failed to remove CLI": "移除 CLI 失败",
    "Install CLI": "安装 CLI",
    "Not installed": "未安装",
    
    # experimental.tsx
    "Native camera preview": "原生摄像头预览",
    
    # feedback.tsx
    "Debug Information": "调试信息",
    "Failed to submit feedback": "提交反馈失败",
    "Failed to upload logs": "上传日志失败",
    "Join the Community": "加入社区",
    "Logs uploaded successfully": "日志上传成功",
    "Not Supported": "不支持",
    "System Information": "系统信息",
    "Upload Logs": "上传日志",
    
    # license.tsx
    "Community Support": "社区支持",
    "No instance ID found": "未找到实例 ID",
    "Perpetual license option": "永久许可证选项",
    "Local-only features": "仅本地功能",
    
    # transcription.tsx
    "Active hints": "激活提示",
    "Add a term": "添加术语",
    "Failed to save transcription hints": "保存转录提示失败",
    
    # integrations/index.tsx
    "Google Drive": "Google Drive",
    "Managed by your organization": "由您的组织管理",
    "Upgrade to Pro": "升级到专业版",
    
    # general.tsx - remaining
    "Cap Pro": "Cap 专业版",
    "Click to copy": "点击复制",
    "Do nothing": "不做任何操作",
    "No available windows to exclude": "没有可排除的窗口",
    "Open editor": "打开编辑器",
    "Show in overlay": "在覆盖层中显示",
    
    # recordings.tsx - remaining
    "No matching": "无匹配",
    "Open link": "打开链接",
    "Recording is potentially corrupted": "录制文件可能已损坏",
    "Show all": "显示全部",
    
    # screenshots.tsx - remaining
    "Open folder": "打开文件夹",
    "Open in editor": "在编辑器中打开",
    
    # hotkeys.tsx - remaining
    "Record area": "录制区域",
    "Record display": "录制显示器",
    "Record window": "录制窗口",
}

for root, dirs, files in os.walk(settings_dir):
    for f in files:
        if not (f.endswith(".tsx") or f.endswith(".ts")):
            continue
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        
        changed = False
        for eng, cn in translations.items():
            if eng in content:
                content = content.replace(eng, cn)
                changed = True
        
        if changed:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            rel = os.path.relpath(path, settings_dir)
            print(f"  {rel}")

print("\ndone")
