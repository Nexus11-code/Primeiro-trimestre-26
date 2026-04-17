def classificar_imc(peso, altura):
    try:
        peso = float(peso)
        altura = float(altura)

        if peso <= 0 or altura <= 0:
            return "Entrada inválida"
        else:
            imc = peso / (altura ** 2)

            if imc < 18.5:
                return "Magro"
            else:
                if imc <= 24.9:
                    return "Normal"
                else:
                    return "Acima do peso"
    except:
        return "Entrada inválida"