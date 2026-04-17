vendas = [10, 15, 20, 7, 8, 13]

soma = 0

for v in vendas:
    if v % 2 == 0:
        soma = soma + v

print("Soma dos pares:", soma)