programa {
    funcao inicio() {  

        real Valordacasa, Salario, prestacao
        inteiro anos, meses

        escreva("Digite o valor da casa: ")
        leia(Valordacasa)

        escreva("Digite o salário do comprador: ")
        leia(Salario)

        escreva("Digite o número de anos para o financiamento: ")
        leia(anos)

        meses = anos * 12
        prestacao = Valordacasa / meses

        se ( prestacao > (Salario * 0.3) ) entao
            escreva("Empréstimo não aprovado.")
        se ( prestacao <= (Salario * 0.3) ) entao
            escreva("Empréstimo aprovado.")

    }
}