import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Admin\.gemini\antigravity\brain\e5782713-7d4f-4278-ad47-f02fc50f5251\.system_generated\steps\16\output.txt', encoding='utf-8') as f:
    data = json.load(f)

def get_by_id(node, target_id):
    if isinstance(node, dict):
        if node.get('id') == target_id: return node
        for child in node.get('children', []):
            res = get_by_id(child, target_id)
            if res: return res
    return None

frame_268 = get_by_id(data, '39:1879')
print(json.dumps(frame_268, ensure_ascii=False, indent=2))
