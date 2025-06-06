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

def edit(choice, listPath):
    data = load_json_file(listPath)
        
    codeEdit = int(input("Insira o código do dado que você deseja editar: "))
    foundData = None
    for item in data:
        if item["codigo"] == codeEdit:
            foundData = item
            break
    if not foundData:
        print("O código não existe! Tente novamente.")
        return
    
    if choice == "1" or choice == "2":  

        newName = input("Insira o novo Nome: ")
        newCpf = input("Insira o novo CPF: ")
        if newCpf != foundData["cpf"] and any(item["cpf"] == newCpf for item in data):
            print("Este CPF já está cadastrado em outro registro! Tente novamente.")
            return

        foundData["nome"] = newName
        foundData["cpf"] = newCpf

        saveData(data, listPath)
        print("Dados atualizados com sucesso.")

    elif choice == "3":
        newName = input("Insira o novo Nome da disciplina: ")
        foundData["nome"] = newName

        saveData(data, listPath)
        print("Dados atualizados com sucesso.")

    elif choice == "4":
        professorData = load_json_file("json/professores.json")
        disciplinaData = load_json_file("json/disciplinas.json")

        
        newProfessorCode = int(input("Insira o novo Código do professor: "))
        if newProfessorCode != foundData["codigo_professor"] and any(item["codigo_professor"] == newProfessorCode for item in data) and any(item["codigo"] == newProfessorCode for item in professorData):
            print("Este codigo já está cadastrado em outro registro! Tente novamente.")
            return
        
        newEnrollmentCode = int(input("Insira o novo Código da disciplina: "))
        if newEnrollmentCode != foundData["codigo_disciplina"] and any(item["codigo_disciplina"] == newEnrollmentCode for item in data) and any(item["codigo"] == newEnrollmentCode for item in disciplinaData):
            print("Este codigo já está cadastrado em outro registro! Tente novamente.")
            return
        
        
        foundData["codigo_professor"] = newProfessorCode
        foundData["codigo_disciplina"] = newEnrollmentCode

        
        saveData(data, listPath)
    
    elif choice == "5":
        classData = load_json_file("json/turmas.json")
        studentData = load_json_file("json/estudantes.json")
        
        newClassCode = int(input("Insira o novo Código da turma: "))
        if newClassCode != foundData["codigo_turma"] and any(item["codigo_turma"] == newClassCode for item in data) and any(item["codigo"] == newClassCode for item in classData):
            print("Código já existe! Tente novamente.")
            return
        
        newStudentCode = int(input("Insira o novo Código do estudante: "))
        if newStudentCode != foundData["codigo_turma"] and any(item["codigo_turma"] == newStudentCode for item in data) and any(item["codigo"] == newStudentCode for item in studentData):
            print("Código já existe! Tente novamente.")
            return
        
        foundData["codigo_turma"] = newClassCode
        foundData["codigo_estudante"] = newStudentCode

        saveData(data, listPath)
