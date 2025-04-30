import json
import os 
from function.include import include
from function.catalogue import catalogue
from function.delete import delete
# list, delete, edit #mudar pra list_items mais tarde

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

studentPath = "json/estudantes.json"
professorPath = "json/professores.json"
disciplinesPath = "json/disciplinas.json"
classesPath = "json/turmas.json"
enrollmentPath = "json/matriculas.json"

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
                        catalogue(studentPath)
                    elif operationChoice == "3":  
                        delete(studentPath)
                    elif operationChoice == "4": 
                        edit("1")
                    elif operationChoice == "5":     
                        print("Voltando para o Menu Principal...")
                        break

                elif menuChoice == "2":  
                    if operationChoice == "1":  
                        include("2", professorPath)
                    elif operationChoice == "2": 
                        catalogue(professorPath)
                    elif operationChoice == "3":  
                        delete(professorPath)
                    elif operationChoice == "4":  
                        edit("1")
                    elif operationChoice == "5":     
                        print("Voltando para o Menu Principal...")
                        break

                elif menuChoice == "3":  
                    if operationChoice == "1":  
                        include("3", disciplinesPath)
                    elif operationChoice == "2": 
                        catalogue( disciplinesPath )
                    elif operationChoice == "3":  
                        delete( disciplinesPath )
                    elif operationChoice == "4":  
                        edit("1")
                    elif operationChoice == "5":     
                        print("Voltando para o Menu Principal...")
                        break

                elif menuChoice == "4":  
                    if operationChoice == "1":  
                        include("4", classesPath)
                    elif operationChoice == "2": 
                        catalogue( classesPath)
                    elif operationChoice == "3":  
                        delete( classesPath )
                    elif operationChoice == "4":  
                        edit("1")
                    elif operationChoice == "5":     
                        print("Voltando para o Menu Principal...")
                        break

                elif menuChoice == "5":  
                    if operationChoice == "1":  
                        include("5", enrollmentPath )
                    elif operationChoice == "2": 
                        catalogue( enrollmentPath )
                    elif operationChoice == "3":  
                        delete( enrollmentPath )
                    elif operationChoice == "4":  
                        edit("1")
                    elif operationChoice == "5":     
                        print("Voltando para o Menu Principal...")
                        break
                
                elif menuChoice == "0":
                    print("Encerrando o programa...")
                    break

                else:
                    print("Opção inexistente")    
            else:
                    print("Opção inexistente") 

