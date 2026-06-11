import re, os

translations = {
    "Instant Mode": "即时模式",
    "Studio Mode": "工作室模式",
    "Screenshot Mode": "截图模式",
    "Start Recording": "开始录制",
    "Stop Recording": "停止录制",
    "Take Screenshot": "截图",
    "Settings": "设置",
    "Recordings": "录制管理",
    "Screenshots": "截图",
    "Help": "帮助",
    "Feedback": "反馈",
    "About": "关于",
    "Changelog": "更新日志",
    "License": "许可证",
    "General": "通用",
    "Hotkeys": "快捷键",
    "Experimental": "实验性",
    "Integrations": "集成",
    "Sign Out": "退出登录",
    "Check for updates": "检查更新",
    "Cancel": "取消",
    "Save": "保存",
    "Delete": "删除",
    "Copy": "复制",
    "Close": "关闭",
    "Confirm": "确认",
    "Done": "完成",
    "Yes": "是",
    "No": "否",
    "OK": "确定",
    "Apply": "应用",
    "Restart": "重启",
    "Learn More": "了解更多",
    "Get Started": "开始使用",
    "Next": "下一步",
    "Skip": "跳过",
    "Continue": "继续",
    "Welcome": "欢迎",
    "Start": "开始",
    "Stop": "停止",
    "Pause": "暂停",
    "Resume": "继续录制",
    "Screen Recording": "屏幕录制",
    "Microphone": "麦克风",
    "Camera": "摄像头",
    "System Audio": "系统音频",
    "Accessibility": "辅助功能",
    "Screen": "屏幕",
    "Window": "窗口",
    "Area": "区域",
    "Display": "显示器",
    "Audio": "音频",
    "Export": "导出",
    "Import": "导入",
    "Share": "分享",
    "Trim": "裁剪",
    "Zoom": "缩放",
    "Background": "背景",
    "Effects": "效果",
    "Text": "文字",
    "Cursor": "光标",
    "Transitions": "转场",
    "Editing": "编辑中",
    "Editor": "编辑器",
    "Preview": "预览",
    "Loading": "加载中",
    "Processing": "处理中",
    "Completed": "已完成",
}

def replace_ui_text(content):
    for eng, cn in translations.items():
        if eng not in content:
            continue
        pattern = re.compile(r"([^a-zA-Z])" + re.escape(eng) + r"([^a-zA-Z])")
        content = pattern.sub(r"\1" + cn + r"\2", content)
    return content

# UI files directories
ui_dirs = [
    "apps/desktop/src/components",
    "apps/desktop/src/routes",
]

desktop_dir = "apps/desktop/src"

# Get all paths recursively from UI dirs, exclude utils/ and store/
count = 0
for root, dirs, files in os.walk(desktop_dir):
    # Skip non-UI directories
    rel = os.path.relpath(root, desktop_dir)
    if rel.startswith("utils") or rel.startswith("store"):
        continue
    
    for f in files:
        if not (f.endswith(".tsx") or f.endswith(".ts")):
            continue
        path = os.path.join(root, f)
        try:
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            new_content = replace_ui_text(content)
            if new_content != content:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new_content)
                count += 1
        except Exception as e:
            print(f"ERR {path}: {e}")

print(f"Updated {count} files")
