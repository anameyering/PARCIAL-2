#Formula dos juros

#Mostra a mensagem, espera o usuário digitar o valor do capital e armazena o valor.
capital = float(input("Digite seu capital (C): "))

#Pede ao usuário a taxa de juros em porcentagem e armazena o valor.
taxa = float(input("Digite a taxa de juros (%): "))

#Pergunta o tempo (meses) em que o dinheiro vai render juros.
tempo = float(input("Digite o tempo em meses (T): "))

#Calcula os juros simples usando a fórmula dos juros simples.
juros = (capital*taxa*tempo) / 100

#Mostra na tela o valor dos juros calculado.
print("O valor dos juros é", juros)
