#Formmula dos juros

#Mostra a mensagem e espera o usuário digitar um valor.
capital = float(input("Digite seu capital (C): "))

#Pede ao usuário a taxa de juros.
taxa = float(input("Digite a taxa de juros (I): "))

#Pergunta o tempo em que o dinheiro vai render juros.
tempo = float(input("Digite o tempo (T): "))

#Calcula os juros simples usando a fórmula dos juros simples.
juros = (capital*taxa*tempo) / 100

#Mostra na tela o valor dos juros calculado.
print("O valor dos juros é", juros)
