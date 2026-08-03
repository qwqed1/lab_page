import os

target_dir = r"d:\Document\lab_page\app"
for root, dirs, files in os.walk(target_dir):
    for f in files:
        if f.endswith(".vue") or f.endswith(".css"):
            path = os.path.join(root, f)
            with open(path, encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()
                if "--uy" in content or "100cqh" in content or "vh" in content:
                    for line in content.splitlines():
                        if "--uy" in line or "bottom:" in line:
                            if "bottom-link" in line or "exact-bottom-link" in line or "--uy" in line:
                                print(f"{path}: {line.strip()}")
