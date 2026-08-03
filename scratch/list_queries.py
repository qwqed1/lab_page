with open(r'd:\Document\lab_page\app\components\FigmaInfoSlide.vue', encoding='utf-8') as f:
    lines = f.readlines()

for idx, l in enumerate(lines):
    if "@media" in l or "@container" in l:
        print(f"Line {idx+1}: {l.strip()}")
