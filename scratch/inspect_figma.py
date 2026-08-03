import json

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

with open('scratch/inspect_result.txt', 'w', encoding='utf-8') as out:
    node = get_by_id(data, '39:1861')
    if node:
        out.write(f"Frame 39:1861 name: {node.get('name')}\n")
        for t in extract_texts(node):
            out.write(t + '\n')
