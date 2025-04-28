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

def saveData(dataList, filePath):
    with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(dataList, f, ensure_ascii=False)

def include(choice, listPath):
    data = load_json_file(listPath)
        
    if choice == "1" or choice == "2":  
        name = input("Insira seu nome: ")
        code = int(input("Insira seu código: "))
        if any(item["codigo"] == code for item in data):
            print("Código já existe! Tente novamente.")
            return
        cpf = input("Insira seu CPF: ")
        if any(item["cpf"] == cpf for item in data):
            print("Este CPF já está cadastrado! Tente novamente.")
            return
        data.append({
            "codigo": code, 
            "nome": name, 
            "cpf": cpf
        })
        saveData(data, listPath)

    elif choice == "3":
        name = input("Insira o nome da disciplina: ")
        code = int(input("Insira seu código: "))
        if any(item["codigo"] == code for item in data):
            print("Código já existe! Tente novamente.")
            return
        data.append({
            "codigo": code, 
            "nome": name
        })
        saveData(data, listPath)
        
    elif choice == "4":

        turmaData = load_json_file("json/turmas.json")
        professorData = load_json_file("json/professores.json")
        disciplinaData = load_json_file("json/disciplinas.json")

        classCode = int(input("Insira o código da turma: "))
        if any(item["codigo"] == classCode for item in turmaData):
            print("Código já existe! Tente novamente.")
            return
        professorCode = int(input("Insira o código do professor: "))
        if any(item["codigo"] == professorCode for item in professorData):
            print("Código já existe! Tente novamente.")
            return
        enrollmentCode = int(input("Insira o código da disciplina: "))
        if any(item["codigo"] == enrollmentCode for item in disciplinaData):
            print("Código já existe! Tente novamente.")
            return
        
        data.append({
            "codigo": classCode, 
            "codigo_professor": professorCode, 
            "codigo_disciplina": enrollmentCode
        })
        saveData(data, listPath)
    
    elif choice == "5":

        turmaData = load_json_file("json/turmas.json")
        estudanteData = load_json_file("json/estudantes.json")

        classCode = int(input("Insira o código da turma: "))
        if any(item["codigo"] == classCode for item in turmaData):
            print("Código já existe! Tente novamente.")
            return
        studentCode = int(input("Insira o código do estudante: "))
        if any(item["codigo"] == studentCode for item in estudanteData):
            print("Código já existe! Tente novamente.")
            return
        data.append({
            "codigo_turma": classCode, 
            "codigo_estudante": studentCode
        })
        saveData(data, listPath)

# def catalogue():
#     print("Listando informações...")

# def delete():
#     print("Excluindo...")

# def edit():
#     print("Editando...")
