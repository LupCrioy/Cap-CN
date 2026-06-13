import re, os

desktop = "apps/desktop/src"

# 1. new-main/index.tsx - remove updater check
path = os.path.join(desktop, "routes/(window-chrome)/new-main/index.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove updater import
content = content.replace('import * as updater from "@tauri-apps/plugin-updater";', '')

# Find and replace the onMount check-for-updates block
import_start = content.find('\tonMount(async () => {')
if import_start > 0:
    # Find the matching closing brace of this onMount
    # The block ends with "});" followed by a line that's not indented
    end_marker = "\t});\n}\n\nfunction MainWindowHelpButton"
    end_pos = content.find(end_marker, import_start)
    if end_pos > 0:
        replacement = '\tonMount(async () => {\n\t\tif (hasChecked) return;\n\t\thasChecked = true;\n\t\t// Update check disabled for offline mode\n\t});\n}\n\nfunction MainWindowHelpButton'
        content = content[:import_start] + replacement + content[end_pos + len(end_marker):]
        print("  fixed new-main/index.tsx")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

# 2. settings.tsx - remove update check
path = os.path.join(desktop, "routes/(window-chrome)/settings.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('import { check } from "@tauri-apps/plugin-updater";', '')

# Find the update check block in settings
# Look for the try/catch that shows "Update Error"
old_block_start = content.find('const update = await check();')
if old_block_start > 0:
    # Find the closing of this try/catch block
    # It ends with the next import or function declaration
    block_end = content.find('\t\t\t\t\t\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t\t\t\t\t}', old_block_start)
    if block_end > 0:
        block_end += len('\t\t\t\t\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t\t\t\t\t}')
        replacement = '\t\t\t\t\t\t\t\t\t\t\t\t\t// Update check disabled for offline mode'
        content = content[:old_block_start - 50] + replacement + content[block_end:]
        print("  fixed settings.tsx")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

# 3. update.tsx - replace entire page with a redirect
path = os.path.join(desktop, "routes/(window-chrome)/update.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('import { check } from "@tauri-apps/plugin-updater";', '')
# Comment out the update check
content = content.replace(
    '\t\t\tconst update = await check();',
    '\t\t\t// update check disabled'
)
content = content.replace(
    '\t\t\tconsole.error("Failed to check for updates:", e);',
    '\t\t\tconsole.error("check updates disabled");'
)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("  fixed update.tsx")

# 4. debug.tsx - remove update check
path = os.path.join(desktop, "routes/debug.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('import { check } from "@tauri-apps/plugin-updater";', '')
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("  fixed debug.tsx")

print("\ndone")
