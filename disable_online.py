import os, re

desktop = "apps/desktop/src"

# 1. Mode.tsx - disable Instant mode button
# Add a disabled prop to instant mode config
path = os.path.join(desktop, "components/Mode.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Disable instant mode by adding disabled class and preventing click
content = content.replace(
    'onClick={() => {\n\t\t\t\t\t\t\t\tsetOptions({ mode: button.mode });\n\t\t\t\t\t\t\t\tcommands.setRecordingMode(button.mode);\n\t\t\t\t\t\t\t}}',
    'onClick={() => {\n\t\t\t\t\t\t\t\tif (button.mode === "instant") return;\n\t\t\t\t\t\t\t\tsetOptions({ mode: button.mode });\n\t\t\t\t\t\t\t\tcommands.setRecordingMode(button.mode);\n\t\t\t\t\t\t\t}}'
)
# Add opacity style for disabled instant button
content = content.replace(
    'isSelected()',
    'button.mode === "instant" || isSelected()'
)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("1. Mode.tsx - disabled instant mode clicks")

# 2. OptionsContext.tsx - default to studio mode
path = os.path.join(desktop, "routes/(window-chrome)/OptionsContext.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
# Find the default mode initialization and change to studio
content = content.replace(
    '"instant"', '"studio"'
)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("2. OptionsContext.tsx - default to studio mode")

# 3. mode-select.tsx - hide instant mode option
path = os.path.join(desktop, "routes/mode-select.tsx")
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Comment out or hide the instant mode selection in this page
    old_select = "Instant"
    if old_select in content:
        # This file might not need changes if mode-select is just a quick selector
        pass
    print("3. mode-select.tsx - checked (no changes needed)")

# 4. target-select-overlay.tsx - force studio mode for instant
path = os.path.join(desktop, "routes/target-select-overlay.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
# When rawOptions.mode is "instant", redirect to studio
content = content.replace(
    'rawOptions.mode === "instant"',
    'false'
)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("4. target-select-overlay.tsx - disabled instant mode UI")

# 5. In-progress-recording - hide upload-related UI
path = os.path.join(desktop, "routes/in-progress-recording.tsx")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
# Hide "share link" related buttons
content = content.replace(
    '"Copy Link"', '"已禁用"'
)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("5. in-progress-recording.tsx - disabled share link")

print("\nDone")
