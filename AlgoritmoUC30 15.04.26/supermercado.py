produto = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))

def calculartotal(produto, produto2):
    return produto + produto2

print(f"O valor total da compra é: R${calculartotal(produto, produto2):.2f}")