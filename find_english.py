import os, re

desktop = "apps/desktop/src"

files_to_check = [
    "components/Mode.tsx",
    "routes/(window-chrome)/onboarding.tsx",
    "routes/(window-chrome)/settings/general.tsx",
    "routes/(window-chrome)/settings/recordings.tsx",
    "routes/(window-chrome)/settings/screenshots.tsx",
    "routes/(window-chrome)/settings/hotkeys.tsx",
    "routes/(window-chrome)/settings/feedback.tsx",
    "routes/(window-chrome)/settings/cli.tsx",
    "routes/(window-chrome)/settings/integrations/index.tsx",
    "routes/(window-chrome)/settings/license.tsx",
]

for file in files_to_check:
    path = os.path.join(desktop, file)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    strings = re.findall(r'\"([A-Z][a-zA-Z][^\"]{10,})\"', content)
    for s in strings:
        if re.search(r"[\u4e00-\u9fff]", s):
            continue
        if len(s) < 15:
            continue
        print(f"{file}: {s[:100]}")
