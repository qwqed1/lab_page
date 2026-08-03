with open(r'd:\Document\lab_page\app\assets\css\main.css', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines):
    if "figma-badge" in l:
        print(f"Line {idx+1}: {l.rstrip()}")
        for k in range(max(0, idx-2), min(len(lines), idx+15)):
            print(f"  {k+1}: {lines[k].rstrip()}")
        print("=" * 60)
