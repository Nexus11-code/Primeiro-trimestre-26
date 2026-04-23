# Sistema de Biblioteca Inclusiva

# Lista de livros
livros = [
    {"nome": "Dom Casmurro", "tipo": "fisico", "disponivel": True},
    {"nome": "Harry Potter", "tipo": "fisico", "disponivel": True},
    {"nome": "O Pequeno Príncipe", "tipo": "audiolivro", "disponivel": True}
]

# mostrar livros
def mostrar_livros():
    print("\n Lista de Livros:")
    for livro in livros:
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f'- {livro["nome"]} ({livro["tipo"]}) - {status}')

# validar entrada
def validar_texto(texto):
    return texto.strip() != ""

# função para pegar livro
def pegar_livro(nome):
    for livro in livros:
        if livro["nome"].lower() == nome.lower():
            return livro
    return None

# função de empréstimo
def emprestar():
    nome = input("Digite o nome do livro: ")

    if not validar_texto(nome):
        print("Nome inválido!")
        return

    livro = pegar_livro(nome)

    if livro:
        if livro["disponivel"]:
            livro["disponivel"] = False
            print(" Livro emprestado com sucesso!")

            # acessibilidade
            if livro["tipo"] == "fisico":
                print(" Dica: Temos versão em audiolivro para acessibilidade!")
        else:
            print(" Livro já está emprestado.")
    else:
        print(" Livro não encontrado.")

# função de devolução
def devolver():
    nome = input("Digite o nome do livro para devolver: ")

    livro = pegar_livro(nome)

    if livro:
        if not livro["disponivel"]:
            livro["disponivel"] = True
            print(" Livro devolvido com sucesso!")
        else:
            print(" Esse livro já está disponível.")
    else:
        print(" Livro não encontrado.")

# menu principal
def menu():
    while True:
        print("\n===== Biblioteca Inclusiva =====")
        print("1 - Ver livros")
        print("2 - Emprestimo de livro")
        print("3 - Devolver livro")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_livros()
        elif opcao == "2":
            emprestar()
        elif opcao == "3":
            devolver()
        elif opcao == "4":
            print("Encerrando sistema...")
            break
        else:
            print(" Opção inválida!")

menu()