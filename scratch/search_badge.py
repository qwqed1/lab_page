import os

target_dir = r"d:\Document\lab_page\app"
for root, dirs, files in os.walk(target_dir):
    for f in files:
        if f.endswith(".vue") or f.endswith(".ts") or f.endswith(".js"):
            path = os.path.join(root, f)
            with open(path, encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()
                if "badge" in content or "slide-11" in content or "Опционально" in content:
                    print("Match in file:", path)
