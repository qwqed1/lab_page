with open(r'd:\Document\lab_page\app\components\FigmaInfoSlide.vue', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines):
    if "exact-bottom-link" in l:
        print(f"Line {idx+1}: {l.rstrip()}")
        for k in range(max(0, idx-3), min(len(lines), idx+10)):
            print(f"  {k+1}: {lines[k].rstrip()}")
        print("=" * 60)
