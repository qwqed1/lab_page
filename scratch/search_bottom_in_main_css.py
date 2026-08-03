with open(r'd:\Document\lab_page\app\assets\css\main.css', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines):
    if "exact-bottom-link" in l:
        print(f"Line {idx+1}: {l.rstrip()}")
