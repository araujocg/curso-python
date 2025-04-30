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

def delete(listPath):

    data = load_json_file(listPath)

    code = int(input("Insira o código que deseja excluir:"))
    for item in data:
        if item["codigo"] == code:
            data.remove(item)
            print(f"Dado com código {code} excluido com sucesso")
            saveData(data, listPath)
            return
        else:
            print("Código não encontrado")