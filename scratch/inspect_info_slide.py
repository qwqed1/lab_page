with open(r'd:\Document\lab_page\app\components\FigmaInfoSlide.vue', encoding='utf-8') as f:
    text = f.read()

print("File size:", len(text))
lines = text.splitlines()
for idx, l in enumerate(lines):
    if "exact-bottom-link" in l or "bottom" in l or "style" in l or "position" in l or "bottom:" in l or "padding-bottom" in l or "margin-bottom" in l:
        print(f"Line {idx+1}: {l.rstrip()}")
