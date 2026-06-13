import re, os

desktop = "apps/desktop/src"
files = [
    "routes/(window-chrome)/settings.tsx",
    "routes/(window-chrome)/settings/general.tsx",
    "routes/(window-chrome)/settings/recordings.tsx",
    "routes/(window-chrome)/settings/screenshots.tsx",
    "routes/(window-chrome)/settings/hotkeys.tsx",
    "routes/(window-chrome)/settings/cli.tsx",
    "routes/(window-chrome)/settings/feedback.tsx",
    "routes/(window-chrome)/settings/license.tsx",
    "routes/(window-chrome)/settings/changelog.tsx",
    "routes/(window-chrome)/settings/experimental.tsx",
    "routes/(window-chrome)/settings/transcription.tsx",
    "routes/editor/ExportPage.tsx",
    "routes/editor/ShareButton.tsx",
]

for file in files:
    path = os.path.join(desktop, file)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    matches = re.findall(r'"([A-Z][a-zA-Z]+(?: [a-zA-Z]+)+)"', content)
    for m in matches:
        if not re.search(r"[\u4e00-\u9fff]", m) and len(m) > 4:
            print(f"{file}: {m}")
            break
print("---check done---")
