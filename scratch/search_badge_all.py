import os

target_dir = r"d:\Document\lab_page"
exclude_dirs = {".git", ".nuxt", "node_modules", "dist", ".output", "scratch", ".vercel"}

for root, dirs, files in os.walk(target_dir):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for f in files:
        if f.endswith(".vue") or f.endswith(".ts") or f.endswith(".js"):
            path = os.path.join(root, f)
            with open(path, encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()
                if "badge" in content or "slide-11" in content or "Опционально" in content:
                    print("Match in file:", path)
