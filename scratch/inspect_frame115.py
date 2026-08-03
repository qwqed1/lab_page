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

def print_tree(node, out, depth=0):
    indent = "  " * depth
    name = node.get('name', '')
    node_id = node.get('id', '')
    node_type = node.get('type', '')
    chars = f" -> '{node.get('characters')}'" if 'characters' in node else ""
    out.write(f"{indent}{node_id} [{node_type}] {name}{chars}\n")
    for child in node.get('children', []):
        print_tree(child, out, depth + 1)

with open('scratch/frame115_tree.txt', 'w', encoding='utf-8') as out:
    f115 = get_by_id(data, '39:1863')
    if f115:
        print_tree(f115, out)
