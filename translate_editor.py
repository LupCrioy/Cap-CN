import os, re

editor_dir = "D:/HANA-WORKSPACE/KFZ-WORKSPACE/Cap-CN/apps/desktop/src/routes/editor"

# Translation map: English -> Chinese (only UI text strings)
translations = {
    # AspectRatioSelect
    "Aspect Ratio": "画面比例",
    
    # CaptionsTab
    "Auto Detect": "自动检测",
    "Best balance for most recordings": "适合大多数录制的最佳平衡",
    "Caption Text": "字幕文字",
    "End Time": "结束时间",
    "Fade Duration Override": "淡入淡出时长覆盖",
    "Failed to download transcription model": "下载转录模型失败",
    "Font Weight": "字体粗细",
    "Generate Captions": "生成字幕",
    "High Accuracy": "高精度",
    "Regenerate Captions": "重新生成字幕",
    "Select a language": "选择语言",
    "Select a model": "选择模型",
    "Selected Caption Override": "选中字幕覆盖",
    "Smallest download": "最小下载体积",
    
    # ConfigSidebar
    "Add custom color": "添加自定义颜色",
    "Animation Style": "动画风格",
    "Audio Controls": "音频控制",
    "Background Blur": "背景模糊",
    "Background Image": "背景图片",
    "Border Color": "边框颜色",
    "Border Opacity": "边框不透明度",
    "Border Width": "边框宽度",
    "Camera Layout": "摄像头布局",
    "Camera Offset": "摄像头偏移",
    "Camera Position": "摄像头位置",
    "Camera Zoom": "摄像头缩放",
    "Corner Style": "边角样式",
    "Cursor Movement Style": "光标移动风格",
    "Cursor Type": "光标类型",
    "Disable Smooth Cursor Movement": "禁用平滑光标移动",
    "Fade Duration": "淡入淡出时长",
    "Failed to save image": "保存图片失败",
    "Failed to set wallpaper": "设置壁纸失败",
    "Heavy Blur": "重度模糊",
    "Hide Camera": "隐藏摄像头",
    "Hide Cursor": "隐藏光标",
    "Hide When Idle": "闲置时隐藏",
    "High Quality SVG Cursors": "高质量 SVG 光标",
    "Improve Mic Quality": "提升麦克风音质",
    "Inactivity Delay": "闲置延迟",
    "Invalid image file type": "无效的图片文件类型",
    "Keep original size during zoom": "缩放时保持原始尺寸",
    "Light Blur": "轻度模糊",
    "Mirror Camera": "镜像摄像头",
    "Mono L": "左声道",
    "Mono R": "右声道",
    "Motion Blur": "运动模糊",
    "Mute Audio": "静音",
    "Open color picker or modal to add a color": "打开拾色器添加颜色",
    "Outside Darkness": "外部暗角",
    "Rounded Corners": "圆角",
    "Selected background": "已选背景",
    "Show cursor": "显示光标",
    "Show hotkeys": "显示快捷键",
    "Shows both screen and camera": "同时显示屏幕和摄像头",
    "Shows only the camera feed": "仅显示摄像头画面",
    "Shows only the screen recording": "仅显示屏幕录制",
    "Size During Zoom": "缩放时尺寸",
    "Smooth Movement": "平滑移动",
    "This Mac": "本机 Mac",
    "This PC": "本机 PC",
    "This device": "本设备",
    "Use Camera Aspect Ratio": "使用摄像头画面比例",
    "Wallpaper option": "壁纸选项",
    "Zoom Mode": "缩放模式",
    
    # Editor
    "Create Preset": "创建预设",
    "Current frame": "当前帧",
    "Rename Preset": "重命名预设",
    "Resize timeline height": "调整时间轴高度",
    "Resize transcript panel": "调整转录面板大小",
    "Set as default": "设为默认",
    "Quit 编辑器": "退出编辑器",
    
    # EditorErrorScreen
    "Recording Needs Recovery": "录制需要恢复",
    "Show Enclosing Folder": "显示所在文件夹",
    "Unable to Open Recording": "无法打开录制",
    
    # ExportPage
    "Advanced Options": "高级选项",
    "Copied to clipboard": "已复制到剪贴板",
    "Copying to clipboard": "正在复制到剪贴板",
    "Cursor track": "光标轨道",
    "Failed to copy recording": "复制录制失败",
    "Failed to delete cancelled file": "删除已取消的文件失败",
    "Failed to upload recording": "上传录制失败",
    "Force FFmpeg decoder": "强制使用 FFmpeg 解码器",
    "Frame Rate": "帧率",
    "Hide options": "隐藏选项",
    "Preparing export": "正在准备导出",
    "Preview unavailable": "预览不可用",
    "Saving to file": "正在保存到文件",
    "Show options": "显示选项",
    "Social Media": "社交媒体",
    "Upload complete": "上传完成",
    "Your Cap has been uploaded successfully": "您的录制已成功上传",
    
    # GradientEditor
    "Grain Scale": "颗粒度",
    
    # Header
    "Failed to regenerate captions": "重新生成字幕失败",
    "Open recording bundle": "打开录制包",
    "Recording imported": "录制已导入",
    "Regenerate captions": "重新生成字幕",
    "Search recordings": "搜索录制",
    
    # KeyboardTab
    "Generate Keyboard Segments": "生成键盘片段",
    "Regenerate Keyboard Segments": "重新生成键盘片段",
    "Selected Segment Override": "选中片段覆盖",
    "Show keyboard": "显示键盘",
    
    # OrganizationDropdown
    "Failed to update organization branding": "更新组织品牌信息失败",
    "Organization branding updated": "组织品牌信息已更新",
    "Unable to load organizations": "无法加载组织列表",
    "Unsupported logo file type": "不支持的 Logo 文件类型",
    
    # PerformanceOverlay
    "Click to copy stats": "点击复制统计信息",
    "Performance stats copied to clipboard": "性能统计已复制到剪贴板",
    
    # Player
    "Crop Video": "裁剪视频",
    "Performance Mode": "性能模式",
    "Select preview quality": "选择预览画质",
    "Toggle Split": "切换分屏",
    "Zoom in": "放大",
    "Zoom out": "缩小",
    
    # ShareButton
    "Open link": "打开链接",
    "Reupload Recording": "重新上传录制",
    "Reupload video": "重新上传视频",
    "Reuploading video": "正在重新上传",
    "Select link": "选择链接",
    
    # text-style
    "Bottom Center": "底部居中",
    "Bottom Left": "底部靠左",
    "Bottom Right": "底部靠右",
    "System Monospace": "系统等宽字体",
    "System Serif": "系统衬线字体",
    "Top Center": "顶部居中",
    "Top Left": "顶部靠左",
    "Top Right": "顶部靠右",
    
    # ui.tsx
    "Coming Soon": "即将推出",
    
    # Timeline
    "Generate captions": "生成字幕",
    "Add track": "添加轨道",
    "Camera Only": "仅摄像头",
    "Hide Camera": "隐藏摄像头",
    "Failed to open track menu": "打开轨道菜单失败",
    "Click to generate zoom segments": "点击生成缩放片段",
    "Dismiss for this session": "本次会话忽略",
    "Generate zoom segments from clicks": "从点击位置生成缩放片段",
    
    # Recording thumbnail (in multiple files)
    "Recording thumbnail": "录制缩略图",
}

# Walk through editor directory
count = 0
for root, dirs, files in os.walk(editor_dir):
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
            rel = os.path.relpath(path, editor_dir)
            count += 1
            print(f"  {rel}")

print(f"\nUpdated {count} files")
