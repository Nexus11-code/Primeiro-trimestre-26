numeros = [80, 20, 30, 20, 40, 90, 50]

print("Lista:", numeros)

quantidade = len(numeros)
print("Quantidade de elementos na lista:", quantidade)

vezes20 = numeros.count(20)
print("O número 20 aparece", vezes20, "vezes na lista.")

posicao30 = numeros.index(30)
print("A posição do número 30 é:", posicao30)

existe100 = 100 in numeros
print("O número 100 esta na lista?", existe100)