import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Admin\.gemini\antigravity\brain\e5782713-7d4f-4278-ad47-f02fc50f5251\.system_generated\steps\16\output.txt', encoding='utf-8') as f:
    data = json.load(f)

def find_frames_with_text(node, target_text):
    results = []
    if isinstance(node, dict):
        chars = node.get('characters', '')
        if target_text in chars:
            results.append((node.get('id'), node.get('name'), chars))
        for child in node.get('children', []):
            results.extend(find_frames_with_text(child, target_text))
    return results

print("Matches for 'Консультация':")
for m in find_frames_with_text(data, 'Консультация'):
    print(m)

print("\nMatches for 'Опционально':")
for m in find_frames_with_text(data, 'Опционально'):
    print(m)
