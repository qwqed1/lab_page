import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\Document\lab_page\app\pages\index.vue', encoding='utf-8') as f:
    text = f.read()

print("File size:", len(text))
# search for doctor or isDoctor or mode or toggle
lines = text.splitlines()
for idx, l in enumerate(lines):
    if any(k in l.lower() for k in ['doctor', 'врач', 'пациент', 'badge', 'опционально', 'slides']):
        print(f"{idx+1}: {l}")
