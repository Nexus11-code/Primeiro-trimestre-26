def soma(a, b):
    try:
        A = float(a)
        B = float(b)
        return A + B
    except TypeError:
        print("Entrada inválida")
        return 0

print(soma(5, 3))
print(soma("5", "3"))
print(soma(5, "x"))