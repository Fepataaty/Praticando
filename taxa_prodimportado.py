def taxacao():
# Atividade proposta no curso de Lógica de Programação de Gustavo Guanabara - Cursos em Vídeo/Youtube

    pergunta = int(input("Você adquiriu algum produto no exterior? \n 1 - Sim \n 2 - Não \n Informe: "))
    
    def calculo():
        produto = str(input("Informe o produto você adquiriu: "))
        if not produto:
            print("Informe o valor do produto")
            calculo()
        else:
            valor_produto = float(input("Informe o valor do produto, em R$: R$"))
            quantia_taxa = valor_produto * 0.4
            
            print(f'Para o produto {produto}, será cobrado 40% do seu valor, totalizando {quantia_taxa}')
            repetiroperacao()
            
    def repetiroperacao():
        repetirOp = int(input("Possui mais produtos adquiridos do exterior? \n 1 - Sim \n 2 - Nâo \n Informe: "))
        if repetirOp == 1:
            calculo()
        if repetirOp == 2:
            print("Operação finalizada. Obrigado!")
        if repetirOp > 2:
            print("Informe a opção correta, por favor!")
            repetiroperacao()
    
    if pergunta == 1:
        calculo()
    elif pergunta == 2:
        print("Pessoa isenta de taxação. Operação finalizada.")
    else:
        print("Informe uma das opções válidas!")
        taxacao()

taxacao() 