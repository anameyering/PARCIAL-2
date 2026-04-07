#Fórmula dos juros

#Mostra a mensagem, espera o usuário digitar o valor do capital e armazena o valor.
capital = float(input("Digite seu capital (C): "))

#Pede ao usuário a taxa de juros em porcentagem e armazena o valor.
taxa = float(input("Digite a taxa de juros (%): "))

#Pergunta o tempo (meses) em que o dinheiro vai render juros.
tempo = float(input("Digite o tempo em meses (T): "))

#Calcula os juros simples usando a fórmula dos juros simples e o montante com a soma do juros e capital.
juros = (capital*taxa*tempo) / 100
montante = capital + juros

#Mostra na tela o valor dos juros calculado e o montante.
print("O valor dos juros é", juros)
print("O valor do montante é", montante)
