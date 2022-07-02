def calculadora():

    operacao = int(input('Informe qual operação deseja fazer: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n Operação: '))

    if operacao > 4 or operacao < 1:
        print('oiiiiii')
    else:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))

        def somar ():
            resultado = num1 + num2
            print(f'{num1} + {num2} = {resultado}')
            repetirOp()

        def subtrair ():
            resultado = num1 - num2
            print(f'{num1} - {num2} = {resultado}')
            repetirOp()

        def multiplicar ():
            resultado = num1 * num2
            print(f'{num1} X {num2} = {resultado}')
            repetirOp()

        def dividir ():
            resultado = num1 // num2
            print(f'{num1} / {num2} = {resultado}')
            repetirOp()
        
        def repetirOp ():
            repetir = int(input('Deseja fazer mais um cálculo? \n 1 - Sim \n 2 - Não \n Escolha: '))
            if repetir == 1:
                calculadora()
            else:
                print('Obrigado por utilizar a calculadora!')

        if operacao == 1:
            somar()
        elif operacao == 2:
            subtrair()
        elif operacao == 3:
            multiplicar()
        elif operacao == 4:
            dividir()
        else:  
            print('Digite uma opção valida!')
calculadora ()