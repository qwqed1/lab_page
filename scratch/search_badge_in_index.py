with open(r'd:\Document\lab_page\app\pages\index.vue', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if "badge" in line:
        print(f"Line {idx+1}: {line.rstrip()}")
