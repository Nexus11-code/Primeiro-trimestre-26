programa {
    funcao inicio() {
        inteiro i, numero, soma
        soma = 0

        escreva("Qual o numero? ")
        leia (numero)

        para(i=1; i<=numero; i++) 
        {
            soma = soma + i
        }
        escreva("soma = ", soma, "\n")

    }
}