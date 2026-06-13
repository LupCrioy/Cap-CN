import re, os

desktop = "apps/desktop/src/routes/editor"
untranslated = []
for root, dirs, files in os.walk(desktop):
    for f in files:
        if not f.endswith((".tsx", ".ts")):
            continue
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                matches = re.findall(r'"([A-Z][a-zA-Z]+(?: [a-zA-Z]+)+)"', line)
                for m in matches:
                    if not re.search(r"[\u4e00-\u9fff]", m) and len(m) > 4:
                        untranslated.append(f"{os.path.relpath(path, desktop)}:{i}: {m}")
                        break
for x in untranslated[:40]:
    print(x)
print(f"\nTotal: {len(untranslated)}")
