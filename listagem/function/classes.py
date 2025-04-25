import json
import os 
def saveData(list, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(list, f, ensure_ascii=False)

def include():
    print("Incluindo informações")
def list():
    print("Listando informações...")

def delete():
    print("Excluindo...")

def edit():
    print("Editando...")
