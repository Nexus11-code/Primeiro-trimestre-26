senha_correta = "123456"
nome = input("Digite seu nome: ")

tentativa1 = input("Digite sua senha: ")

if tentativa1 == senha_correta:
    print(f"Olá, {nome}. Seja bem-vindo ao nosso banco!")
else:
    print("Senha incorreta! Você ainda tem 2 tentativas.")
    
    tentativa2 = input("Digite sua senha novamente: ")
    
    if tentativa2 == senha_correta:
        print(f"Olá, {nome}. Seja bem-vindo ao nosso banco!")
    else:
        print("Senha incorreta! Você ainda tem 1 tentativa.")
        
        tentativa3 = input("Digite sua senha novamente: ")
        
        if tentativa3 == senha_correta:
            print(f"Olá, {nome}. Seja bem-vindo ao nosso banco!")
        else:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")