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

def extract_texts(node):
    texts = []
    if isinstance(node, dict):
        if node.get('type') == 'TEXT' and 'characters' in node:
            texts.append(f"{node.get('id')} [{node.get('name')}]: {node.get('characters')}")
        for child in node.get('children', []):
            texts.extend(extract_texts(child))
    return texts

doctors_sec = get_by_id(data, '202:100')
if doctors_sec:
    for child in doctors_sec.get('children', []):
        print(f"--- Doctor Frame {child.get('id')} ({child.get('name')}) ---")
        for t in extract_texts(child):
            print("  ", t)
