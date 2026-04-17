frase = input("Digite uma frase: ")

contador = 0

for letra in frase:
    if letra in "aeiouAEIOU":
        contador += 1

print("Quantidade de vogais:", contador)