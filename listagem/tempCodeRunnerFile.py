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

                if menuChoice == "1":  # Se for "Estudantes"
                    if operationChoice == "1":  # Incluir estudante
                        include("1", studentPath)
                    elif operationChoice == "2":  # Listar estudantes
                        list()
                    elif operationChoice == "3":  # Excluir estudante
                        delete("")
                    elif operationChoice == "4":  # Editar estudante
                        edit("1")
                    elif operationChoice == "5":     
                        print("Voltando para o Menu Principal...")
                    break

                elif menuChoice == "2":  # Se for "Professores"
                    if operationChoice == "1":  # Incluir professor
                        include("2", professorPath)
                    elif operationChoice == "2":  # Listar professores
                        list()
                    elif operationChoice == "3":  # Excluir professor
                        delete("")
                    elif operationChoice == "4":  # Editar professor
                        edit("1")
                    elif operationChoice == "5":     
                        print("Voltando para o Menu Principal...")
                    break
                else:
                    print("Opção inexistente")    
            else:
                    print("Opção inexistente") 