import json
def salvar_infos(lista, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False)
#Função para ler os dados do json


def ler_infos(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            lista = json.load(f)
        return lista
    except:
        return []
lista_estudante = ler_infos("estudantes.json")
lista_disc = ler_infos("disciplina.json")



#Função dos Menus
def mostrarmenu(menus):
    for opcao, categoria in menus.items():
        print(f"{opcao}: {categoria}")



    
#Função para incluir os nomes e verificar se ja estão na lista
def incluir(arquivo):
    nome = input("Insira seu nome:")
    cod_est = int(input("Insira seu código:"))
    if any(item["Código"] == cod_est for item in arquivo):
        print("Código já existe! Tente novamente.")
        return
    cpf = input("Insira seu CPF:")
    if any(item["CPF"] == cpf for item in arquivo):
        print("Este CPF já está cadastrado! Tente novamente.")
        return
    arquivo.append({f"Código": cod_est, "Nome": nome, "CPF": cpf})
    salvar_infos(arquivo, "estudantes.json")

# def incluir_disc():
#     cod_disc = int(input("Insira o código da disciplina:"))
#     nome_disc = input("Insira o nome da disciplina:")
#     if any(item["Código"] == cod_disc for item in lista_disc):
#         print("Código já existe! Tente novamente.")
#     if any(item["Nome da disciplina"] == nome_disc for item in lista_disc):
#         print("Esta disciplina já está cadastrada! Tente novamente.")
#         return
#     lista_disc.append({f"Código": cod_disc, "Nome da disciplina": nome_disc,})
#     salvar_infos(lista_disc, "disciplina.json")
# def listar_disc():
#     if not lista_disc:
#         print("A lista está vazia.")
#     else:
#         for item in lista_disc:
#             print(f"Dados: {item}")
# def excluir_disc():
#     delete = int(input("Insira o código que deseja excluir:"))
#     for item in lista_disc:
#         if item["Código"] == delete:
#             lista_disc.remove(item)
#             print(f"Disciplina com código {delete} excluido com sucesso")
#             salvar_infos(lista_disc, "disciplina.json")
#             return
#         else:
#             print("Código não encontrado")
# def editar_disc():
#     edit = int(input("Insira o código que você deseja alterar:"))
#     for item in lista_disc:
#         if item["Código"] == edit:
#             lista_disc.remove(item)
#             incluir_disc()
#             print("Informações alteradas com sucesso")
#             salvar_infos(lista_disc, "disciplina.json")
#             return
#     else:
#         print("Código não encontrado")



#Função de listar
def listar_info():
    if not lista_estudante:
        print("A lista está vazia.")
    else:
        for item in lista_estudante:
            print(f"Dados: {item}")



#Função para excluir
def excluir():
    delete = int(input("Insira o código que deseja excluir:"))
    for item in lista_estudante:
        if item["Código"] == delete:
            lista_estudante.remove(item)
            print(f"Dado com código {delete} excluido com sucesso")
            salvar_infos(lista_estudante, "estudantes.json")
            return
        else:
            print("Código não encontrado")
#Função para editar os dados
def editar():
    edit = int(input("Insira o código que você deseja alterar:"))
    for item in lista_estudante:
        if item["Código"] == edit:
            lista_estudante.remove(item)
            # incluir()
            print("Informações alteradas com sucesso")
            salvar_infos(lista_estudante, "estudantes.json")
            return
    else:
        print("Código não encontrado")
alunos = []
disciplinas = []
#menus
menuprincipal = {
    "1": "Estudantes",
    "2": "Disciplina",
    "3": "Professores",
    "4": "Turmas",
    "5": "Matrícula",
    "0": "Sair"
}
menuoperacoes = {
    "1": "Incluir",
    "2": "Listar",
    "3": "Excluir",
    "4": "Editar",
    "5": "Sair",
}
#Looping menu principal
while True:
    print("---Menu Principal---")
    mostrarmenu(menuprincipal)
    escolha = input("Informe a opção desejada:").strip()
    if escolha == "0":
        print("Encerrando o programa...")
        break
    elif escolha in menuprincipal:
        print(f"Você escolheu a opção: {menuprincipal[escolha]}\nAbrindo o menu de operações")
    #Looping do menu de operações
        while True:
            print("---Menu de Operações----")
            mostrarmenu(menuoperacoes)
            segundaopcao = input("Insira a segunda opção desejada: ").strip()
            if segundaopcao in menuoperacoes:
                print(f"Você escolheu a opção {menuoperacoes[segundaopcao]}")
                if escolha == "1":
                    if segundaopcao == "1":
                        incluir_aluno()
                    elif segundaopcao == "2":
                        listar_info()
                    elif segundaopcao == "3":
                        excluir()
                    elif segundaopcao == "4":
                        editar()
                    elif escolha == "2":
                        if segundaopcao == "1":
                            incluir_disc()
                        elif segundaopcao == "2":
                            listar_disc()
                        elif segundaopcao == "3":
                            excluir_disc()
                        elif segundaopcao == "4":
                            editar()
                    elif segundaopcao == "5":
                        print("Voltando para o Menu Principal...")
                        break
            else:
                print("Opção inexistente")
    else:
        print("Opção inexistente")