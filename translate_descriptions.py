import os, re

desktop = "apps/desktop/src"

# Mode descriptions in Mode.tsx
path = os.path.join(desktop, "components/Mode.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ('"No rendering required — uploads on the fly so you can share the link the moment you stop."',
     '"无需渲染——边录边传，停止录制即刻获得分享链接。"'),
    ('"Records at the highest quality for local rendering later. Opens the Cap editor when you\'re done."',
     '"以最高画质本地录制，录制完成后自动打开编辑器。"'),
    ('"Capture and annotate stills."',
     '"截取屏幕并添加标注。"'),
    ('"Recording mode info"',
     '"录制模式说明"'),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"  Mode.tsx: translated")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

# Settings general descriptions
path = os.path.join(desktop, "routes/(window-chrome)/settings/general.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

general_translations = [
    ('"Match Cap to your system theme or pick a fixed look."', '"让 Cap 跟随系统主题，或选择固定外观。"'),
    ('"Choose how Cap shows up on your system."', '"选择 Cap 在系统中的显示方式。"'),
    ('"Always show dock icon"', '"始终显示 Dock 图标"'),
    ('"Keep Cap in the dock even when no windows are open."', '"即使没有窗口打开也保留 Cap 在 Dock 中。"'),
    ('"System notifications"', '"系统通知"'),
    ('"Show notifications for clipboard copies, saved files, and more."', '"显示复制、保存等操作的通知。"'),
    ('"Behaviour while you record and after you stop."', '"录制中及录制后的行为设置。"'),
    ('"Wait before the recording starts."', '"录制开始前的等待时间。"'),
    ('"Main window when recording starts"', '"录制开始时主窗口"'),
    ('"What happens to the main window once a recording begins."', '"录制开始后主窗口的行为。"'),
    ('"After a Studio recording"', '"工作室模式录制完成后"'),
    ('"What happens once you stop a Studio recording."', '"停止工作室模式录制后的行为。"'),
    ('"After deleting a recording"', '"删除录制后"'),
    ('"Whether the recording window should reopen."', '"是否重新打开录制窗口。"'),
    ('"Reopen recording window"', '"重新打开录制窗口"'),
    ('"Crash-recoverable recording"', '"崩溃可恢复录制"'),
    ('"Record in fragments that can be recovered after a crash or power loss."', '"以分段方式录制，崩溃或断电后可恢复。"'),
    ('"Custom cursor capture (Studio)"', '"自定义光标捕获（工作室模式）"'),
    ('"Capture cursor state separately so you can adjust size and smoothing in the editor."', '"单独捕获光标状态，可在编辑器中调整大小和平滑度。"'),
    ('"Auto zoom on clicks"', '"点击时自动缩放"'),
    ('"Automatically add zoom segments around mouse clicks in Studio recordings."', '"在工作室模式录制中自动在鼠标点击处添加缩放片段。"'),
    ('"Capture keyboard presses"', '"捕获键盘按键"'),
    ('"Record key presses so you can add keyboard overlays in the editor."', '"记录按键操作，可在编辑器中添加键盘覆盖层。"'),
    ('"Max capture framerate"', '"最大捕获帧率"'),
    ('"Maximum framerate for screen capture."', '"屏幕捕获的最大帧率。"'),
    ('"Telemetry"', '"遥测"'),
    ('"Cap uses anonymous telemetry to improve reliability and fix bugs."', '"Cap 使用匿名遥测数据来改进可靠性和修复问题。"'),
    ('"Lower bitrate to keep older or low-power machines smooth."', '"低比特率，适合老旧或低性能设备。"'),
    ('"Older Intel Macs, 8GB MacBook Air, weaker laptops."', '"旧款 Intel Mac、8GB MacBook Air、较弱笔记本。"'),
    ('"Sharp footage with sensible CPU and disk usage."', '"画质清晰，CPU 和磁盘占用适中。"'),
    ('"Most modern Macs and PCs with 16GB+ RAM."', '"适合大多数 16GB+ 内存的现代电脑。"'),
    ('"Maximum detail for color-graded, large-display edits."', '"最高细节，适合调色和大屏编辑。"'),
    ('"Smallest size, low bandwidth."', '"最小体积，低带宽。"'),
    ('"Recommended. Sharp on most networks."', '"推荐。在大多数网络下画质清晰。"'),
    ('"More detail for desktop content."', '"更多细节，适合桌面内容。"'),
    ('"Max clarity. Needs fast upload."', '"最高清晰度，需要快速上传。"'),
    ('"Pick the right profile for local Studio recordings."', '"为本地工作室模式录制选择合适的配置。"'),
    ('"Default project name"', '"默认项目名称"'),
    ('"Template used for new recordings and exported files."', '"用于新建录制和导出文件的名称模板。"'),
    ('"Excluded windows"', '"排除的窗口"'),
    ('"Hide windows from recordings."', '"从录制中隐藏指定窗口。"'),
    ('"Remove excluded window"', '"移除排除的窗口"'),
]

for old, new in general_translations:
    if old in content:
        content = content.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("  general.tsx: translated")

# Recordings settings
path = os.path.join(desktop, "routes/(window-chrome)/settings/recordings.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

recording_translations = [
    ('"Manage your recordings and perform actions."', '"管理你的录制文件。\u200b"'),
    ('"Search recordings"', '"搜索录制"'),
    ('"Recording thumbnail"', '"录制缩略图"'),
    ('"Open recording bundle"', '"打开录制包"'),
    ('"Are you sure you want to delete this recording?"', '"确定要删除此录制吗？"'),
]

for old, new in recording_translations:
    if old in content:
        content = content.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("  recordings.tsx: translated")

# Screenshots settings
path = os.path.join(desktop, "routes/(window-chrome)/settings/screenshots.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

screenshot_translations = [
    ('"Manage your screenshots and perform actions."', '"管理你的截图。\u200b"'),
    ('"Search screenshots"', '"搜索截图"'),
    ('"Are you sure you want to delete this screenshot?"', '"确定要删除此截图吗？"'),
]

for old, new in screenshot_translations:
    if old in content:
        content = content.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("  screenshots.tsx: translated")

# Hotkeys settings  
path = os.path.join(desktop, "routes/(window-chrome)/settings/hotkeys.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

hotkeys_translations = [
    ('"Cycle recording mode"', '"切换录制模式"'),
    ('"Open recording picker"', '"打开录制选择器"'),
    ('"Screenshot current display"', '"截取当前屏幕"'),
    ('"Screenshot current window"', '"截取当前窗口"'),
    ('"Screenshot area picker"', '"区域截图"'),
    ('"Configure system-wide keyboard shortcuts to control Cap."', '"配置系统级快捷键来控制 Cap。"'),
]

for old, new in hotkeys_translations:
    if old in content:
        content = content.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("  hotkeys.tsx: translated")

print("\nDone")
