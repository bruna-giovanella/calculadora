
def calculadora():
    print('Bem vindo :)\nAs operações disponíveis são:')

    # Menu de opções 
    def action():
        global operacao 
        operacao = int(input('\n1-adição\n2-subtração\n3-multiplicação\n4-divisão\n\nQual operação você deseja realizar? '))
        print('operacao dentro',operacao) #TESTE


        if operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4:
            print('O valor informado é invalido :(\nPor favor, insere um novo valor, válido')
            return action 
        else: 
            print('Certo! Para prosseguirmos, preciso que informe dois valores')
            global a
            global b
            a = float(input('valor a: '))
            b = float(input('valor b: '))
    
    action()
    

    # Funções de operação
    def adicao(a,b):
        soma = a+b
        print(f'{a} + {b} = {soma}')

    def subtracao(a,b):
        diferenca = a-b
        print(f'{a} - {b} = {diferenca}')


    def multiplicacao(a,b):
        produto = a*b
        print(f'{a} * {b} = {produto}')

    def divisao(a,b):
        quociente = a/b
        print(f'{a} / {b} = {quociente}')


    # Chamando a função de acordo com a opção selecionada
    if operacao == 1:
        print(a,b)
        adicao(a,b)
    if operacao == 2:
        return subtracao
    if operacao == 3:
        return multiplicacao
    if operacao == 4:
        return divisao
        

calculadora()



