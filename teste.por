programa {
    funcao inicio() {
        inteiro mes

        escreva("Digite o número do mês (1-12): ")
        leia(mes)

        escolha(mes) {
            caso 1: caso 3: caso 5: caso 7: caso 8: caso 10: caso 12:
                escreva("O mês tem 31 dias. \n")
                pare
            
            caso 4: caso 6: caso 9: caso 11:
                escreva("O mês tem 30 dias. \n")
                pare
            
            caso 2:
                escreva("O mês tem 28 dias. \n")
                pare

            caso  contrario:
                escreva("Número do mês inválido. Por favor, digite um número entre 1 e 12. \n")  
        }
    }
}