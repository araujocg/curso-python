import json
import os 
def saveData(list, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(list, f, ensure_ascii=False)

def include(choice, listPath):
    file_path = f"json/{listPath}"
    
    # Lê os dados direto do arquivo, se existir
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
        
    if choice == "1" or choice == "2":  
        nome = input("Insira seu nome: ")
        codigo = int(input("Insira seu código: "))

        
        if any(item["codigo"] == codigo for item in data):
            print("Código já existe! Tente novamente.")
            return
        
        cpf = input("Insira seu CPF: ")
       
        if any(item["cpf"] == cpf for item in data):
            print("Este CPF já está cadastrado! Tente novamente.")
            return
        
        data.append({"codigo": codigo, "nome": nome, "cpf": cpf})
        saveData(data, file_path)
def list():
    print("Listando informações...")

def delete():
    print("Excluindo...")

def edit():
    print("Editando...")
