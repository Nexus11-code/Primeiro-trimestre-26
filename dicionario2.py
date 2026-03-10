matricula1 = 2026001
nome1 = "Álvaro Pereira"
telefone = "9602-1102"

aluno = {
    "matricula": matricula1,
    "nome": nome1,
    "telefone": telefone,
}

print(aluno)

contato = {
    "@camilaqueiroz": "camila queiroz",
    "@brunamarquezine": "bruna M.",
    "@sheronmenezes": "sheron M.",
    "@paolaoliveira": "paola O.",
}

print(contato)
print(type(contato))

print(contato.get("@paolaoliveira"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "não encontrado"))

contato["@giovanna"] = "giovanna"
print("apos add: ", contato)

contato["@paolaoliveira"] = "paola Oliveira"
print("apos update de paola: ", contato)

contato.update({
    "@brunamarquezine": "bruna marquezine",
    "@camilaqueiroz": "camila Q.",
})

print("apos atualização:", contato)

removido = contato.pop("@paolaoliveira", None)
print(f"removido: {removido}")
print("apos o pop:", contato)

if "@camilaqueiroz" in contato:
    del contato["@camilaqueiroz"]
    print("apos o del", contato)

copia = dict(contato)
contato.clear()
print("apos clear: ", contato)
print("copia: ", copia)

print("numero de contatos (copia): ", len(copia))

if "@joao" in copia:
    print(f'encontrado: {copia["@joao"]}')

if "@inexistente" in copia:
    print("Existe")
else:
    print("nao existe.")