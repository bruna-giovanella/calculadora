while True:
    
    def calculadora():
        print('Bem vindo :)\nAs operações disponíveis são:')

        # Menu de opções 
        def action():
            global operacao 
            operacao = int(input('\n1-adição\n2-subtração\n3-multiplicação\n4-divisão\n\nQual operação você deseja realizar? '))

            if operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4:
                print('O valor informado é invalido :(\nPor favor, insere um novo valor, válido')
                action() 
            else: 
                print('Certo! Para prosseguirmos, preciso que informe os valores que serão operados\nSepare os valores com espaços')
                global numeros
                numeros = list(map(float, input('valores: ').split()))
        
        action()
        

        # Funções de operação
        def adicao(*args):
            soma = sum(args)
            print(f'adicao = {soma}')
            

        def subtracao(*args):
            diferenca = args[0]
            for i in args[1:]:
                diferenca -= i
            print(f'subtração = {diferenca}')


        def multiplicacao(*args):
            produto = args[0]
            for i in args[1:]:
                produto *= i
            print(f'multiplicacao = {produto}')

        def divisao(*args):
            quociente = args[0]
            for i in args[1:]:
                quociente /= i
            print(f'divisao = {quociente}')


        # Chamando a função de acordo com a opção selecionada
        if operacao == 1:
            adicao(*numeros)
        if operacao == 2:
            subtracao(*numeros)
        if operacao == 3:
            multiplicacao(*numeros)
        if operacao == 4:
            divisao(*numeros)

        

    calculadora()
    end = input('Deseja realizar uma nova operação? (s/n) ')
    if end == 'n':
        break
    else:
        calculadora
