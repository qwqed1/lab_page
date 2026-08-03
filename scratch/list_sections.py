import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Admin\.gemini\antigravity\brain\e5782713-7d4f-4278-ad47-f02fc50f5251\.system_generated\steps\16\output.txt', encoding='utf-8') as f:
    data = json.load(f)

for child in data.get('children', []):
    print(f"Top-level: {child.get('id')} [{child.get('type')}] {child.get('name')}")
    if child.get('type') == 'SECTION':
        for sc in child.get('children', []):
            print(f"  - {sc.get('id')} [{sc.get('type')}] {sc.get('name')}")
