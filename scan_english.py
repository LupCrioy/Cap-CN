import os, re

desktop = "apps/desktop/src"

# Focus on main UI areas that users see
scan_dirs = [
    "routes/editor",
    "routes/(window-chrome)/settings",
    "components",
    "routes/(window-chrome)/new-main",
    "routes/(window-chrome)/onboarding.tsx",
]

# Skip files that are purely technical
skip_patterns = [
    "context.ts", "utils.ts", "config.ts", "socket.ts",
    "tauri.ts", "queries.ts", "auth.ts", "analytics.ts",
    "events.ts", "export.ts", "importMedia.ts",
    "titlebar-state.ts", "macos-window-material.ts",
    "organization-branding.ts",
]

# English phrases that are clearly UI text and should be translated
ui_text_patterns = []

print("=== 未汉化的 UI 文本 ===\n")

for item in scan_dirs:
    path = os.path.join(desktop, item)
    if not os.path.exists(path):
        continue
    
    if os.path.isfile(path):
        files = [path]
    else:
        files = []
        for root, dirs, fnames in os.walk(path):
            for f in fnames:
                if f.endswith((".tsx", ".ts")):
                    files.append(os.path.join(root, f))
    
    for filepath in files:
        filename = os.path.basename(filepath)
        rel = os.path.relpath(filepath, desktop)
        
        # Skip technical files
        skip = False
        for s in skip_patterns:
            if s in rel or s in filename:
                skip = True
                break
        if skip:
            continue
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Find English quoted strings that are UI text
        # Match "Word" or 'Word' patterns, skip code identifiers
        strings = re.findall(r'"(?:[A-Z][a-zA-Z]+(?:\s+[a-zA-Z]+)*)"', content)
        
        ui_strings = []
        for s in strings:
            text = s.strip('"')
            # Skip very short strings
            if len(text) < 3:
                continue
            # Skip pure code identifiers (camelCase, PascalCase with no spaces)
            if re.match(r'^[a-z]+[A-Z]', text):
                continue
            # Skip single words that are likely code
            if ' ' not in text and len(text) > 15:
                continue
            # Skip strings that already contain Chinese
            if re.search(r'[\u4e00-\u9fff]', text):
                continue
            # Skip common code patterns
            if text in ['default', 'error', 'Error', 'success', 'cancel']:
                continue
            # Skip strings in import statements (check context)
            
            # Check if this text appears in a UI context (not import/type)
            # Simple heuristic: if it has spaces and capital letter, likely UI text
            if ' ' in text and text[0].isupper():
                ui_strings.append(text)
            elif ' ' in text and len(text) > 5:
                ui_strings.append(text)
        
        if ui_strings:
            print(f"\n--- {rel} ---")
            for s in sorted(set(ui_strings)):
                if s not in ['Settings', 'General', 'Hotkeys', 'Feedback', 'Changelog', 
                             'Experimental', 'License', 'Integrations', 'Cancel', 'Save',
                             'Delete', 'Close', 'Yes', 'No', 'OK', 'Done', 'Apply', 'Help',
                             'About', 'Search', 'Upload', 'Share', 'Export', 'Import',
                             'Preview', 'Start', 'Stop', 'Pause', 'Resume', 'Text', 'Copy',
                             'Rename', 'Open', 'Quality', 'Resolution', 'Format']:
                    print(f"  \"{s}\"")

print("\n=== 以上是剩余的英文 UI 文本 ===")
