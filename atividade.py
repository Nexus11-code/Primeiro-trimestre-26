#Soma

def SomaDeNumeros(nuemero1, numero2):
    soma = numero1 + numero2
    produto = numero1 * numero2

    print("Soma: ", soma)
    print("resultado: ", produto)

#Calcular Salario

def calcularsalario(ValorHora, HoraTrabalhada):
    SalarioTotal= ValorHora * HoraTrabalhada
    return SalarioTotal

total = calcularsalario(60, 120)
print("Salario total: ", total)