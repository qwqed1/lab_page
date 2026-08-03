import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('extracted_texts.json', encoding='utf-8') as f:
    texts = json.load(f)

print("Keys in extracted_texts.json:", len(texts))
for k, v in list(texts.items())[:20]:
    print(f"{k}: {v[:80] if isinstance(v, str) else v}")
