import json
import os 
from function.student import include, list, delete, edit

#menus
menu = {
    "1": "Estudantes",
    "2": "Professores",
    "3": "Disciplina",
    "4": "Turmas",
    "5": "Matrícula",
    "0": "Sair"
}
operations = {
    "1": "Incluir",
    "2": "Listar",
    "3": "Excluir",
    "4": "Editar",
    "5": "Sair",
}
studentPath = "estudantes.json"
professorPath = "professores.json"
disciplinesPath = "disciplinas.json"
classesPath = "turmas.json"
enrollmentPath = "matriculas.json"

def readData(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            list = json.load(f)
        return list
    except:
        return []
    
listStudent = readData(studentPath)
listProf = readData(professorPath)


def showMenu(menus):
    for opcao, categoria in menus.items():
        print(f"{opcao}: {categoria}")

while True:
    print("---Menu Principal---")
    showMenu(menu)
    menuChoice = input("Informe a opção desejada:").strip()
    if menuChoice == "0":
        print("Encerrando o programa...")
    elif menuChoice in menu:
        print(f"Você escolheu a opção: {menu[menuChoice]}\nAbrindo o menu de operações")
    #Looping do menu de operações
        while True:
            print("---Menu de Operações----")
            showMenu(operations)
            operationChoice = input("Insira a segunda opção desejada: ").strip()
            if operationChoice in operations:
                print(f"Você escolheu a opção {operations[operationChoice]}")

                if menuChoice == "1":  
                    if operationChoice == "1":  
                        include("1", studentPath)
                    elif operationChoice == "2":  
                        list()
                    elif operationChoice == "3":  
                        delete("")
                    elif operationChoice == "4": 
                        edit("1")
                    elif operationChoice == "5":     
                        print("Voltando para o Menu Principal...")
                    break

                elif menuChoice == "2":  
                    if operationChoice == "1":  
                        include("2", professorPath)
                    elif operationChoice == "2": 
                        list()
                    elif operationChoice == "3":  
                        delete("")
                    elif operationChoice == "4":  
                        edit("1")
                    elif operationChoice == "5":     
                        print("Voltando para o Menu Principal...")
                    break
                else:
                    print("Opção inexistente")    
            else:
                    print("Opção inexistente") 

