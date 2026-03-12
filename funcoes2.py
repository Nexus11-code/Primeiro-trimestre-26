print("Python é facil")
print("Python é facil")
print("Python é facil")

def exibirMensagem():
    print("Olá, mundo!")

exibirMensagem()

def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Ana")
saudar("Bruno")

def exibirMensagem(nome, mensagem):
    print(f"{mensagem}, {nome}")

exibirMensagem("Ana", "Bom dia")

exibirMensagem(nome = "Bruno", mensagem = "Boa noite")

def calculadorMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado = calcularMedia(8.0, 9.0)
print (f"Média: {resultado}")