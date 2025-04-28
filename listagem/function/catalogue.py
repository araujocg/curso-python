import json
import os 

def load_json_file(path):
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def saveData(list, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(list, f, ensure_ascii=False)


def catalogue(listPath):
    
    data = load_json_file(listPath)

    for i, item in enumerate(data, start=1):
        info = " | ".join(f"{k}: {v}" for k, v in item.items())
        print(f"Item {i}: {info}")

