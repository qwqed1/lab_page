import os

target_dir = r"d:\Document\lab_page\app"
for root, dirs, files in os.walk(target_dir):
    for f in files:
        if f.endswith(".vue") or f.endswith(".ts") or f.endswith(".json"):
            path = os.path.join(root, f)
            with open(path, encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()
                if "Консультация" in content or "консультация" in content or "Опционально" in content or "опционально" in content:
                    print("Found in:", path)
