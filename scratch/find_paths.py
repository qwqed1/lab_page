import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Admin\.gemini\antigravity\brain\e5782713-7d4f-4278-ad47-f02fc50f5251\.system_generated\steps\16\output.txt', encoding='utf-8') as f:
    data = json.load(f)

def find_node_path(node, target_id, path=[]):
    if isinstance(node, dict):
        if node.get('id') == target_id:
            return path + [node]
        for child in node.get('children', []):
            res = find_node_path(child, target_id, path + [node])
            if res: return res
    return None

for node_id in ['12:95', '12:229', '12:609', '12:785', '39:1878']:
    p = find_node_path(data, node_id)
    if p:
        path_str = " -> ".join([f"{n.get('id')} ({n.get('name')})" for n in p])
        print(f"Path for {node_id}:\n{path_str}\n")
