notas = [7.5, 8.0, 9.5, 6.0, 8.5]
print("Notas: ", notas)

print("Maior: ", min(notas))
print("Menor: ", min(notas))
print("Soma: ", sum(notas))
print("Média: ", sum(notas) / len(notas))

nomes = ["Adriano", "Alexandre", "Paulo", "Thiago"]

# apenas o elemento
print("Usando FOR simples: ")
for nome in nomes:
    print(f"Olá, {nomes}!")

# Índice e elemento
print ("\n usando enumerate: ")
for indice, nome in enumerate(nomes):
    print(f"Posição {indice}: {nome}")

    original = ["A", "B", "C"]
    copia = list(original)

    print("Original: ", original)
    print("Cópia: ", copia)
    print("São iguais: ", original == copia)

    copia.append("D")
    print("Original", original)
    print("Cópia: ", copia)
    print("São iguais: ", original == copia)