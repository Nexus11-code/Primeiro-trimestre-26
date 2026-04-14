def divisao(x, y):
    try:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            return "Entrada invalida"
        if y == 0:
            return "Nao divida por zero!"
        return x / y
    except Exception:
        return "Deu algum erro"