while True:
    print("1-soma 2-sub 3-mult 4-div 5-sair")
    opcao = input("Opção: ")

    if opcao == "5":
        break

    try:
        a = float(input("Num1: "))
        b = float(input("Num2: "))

        if opcao == "1":
            print(a + b)
        elif opcao == "2":
            print(a - b)
        elif opcao == "3":
            print(a * b)
        elif opcao == "4":
            print(a / b)
    except:
        print("Erro")