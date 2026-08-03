import os

target_dir = r"d:\Document\lab_page\app"
for root, dirs, files in os.walk(target_dir):
    for f in files:
        if f.endswith(".vue") or f.endswith(".css"):
            path = os.path.join(root, f)
            with open(path, encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()
                if "Все вопросы" in content or "Все материалы" in content or "exact-bottom-link" in content:
                    print("Match in file:", path)
