import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Document\lab_page\app\pages\index.vue', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if any(keyword in line for keyword in ["Консультация", "консультация", "Опционально", "опционально"]):
        print(f"Line {idx+1}: {line.strip()}")
        for k in range(max(0, idx-5), min(len(lines), idx+15)):
            print(f"  {k+1}: {lines[k].rstrip()}")
        print("-" * 50)
