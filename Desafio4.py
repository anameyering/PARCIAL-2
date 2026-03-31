#Calculadora simples

#As duas linhas seguintes mostra uma mensagem para o usuário informar dois números separadamente e aguarda a resposta.
n1 = float(input("selecione número 1: "))
n2 = float(input("selecione número 2: "))

#Mostra mensagem para o usuário escolher a operação.
operação = input("escolha uma operação [soma, subtração, multiplicação ou divisão]: ")

#Se for escolhido soma, o Pynthon soma n1 e n2 e mostra o resultado na tela.
if operação == "soma":
  print( n1 + n2)

#Se for escolhido subtração, o Pynthon subtrai n1 e n2 e mostra o resultado na tela.
elif operação == "subtração":
  print( n1 - n2)

#Se for escolhido multiplicação, o Pynthon multiplica n1 por n2 e mostra o resultado na tela.
elif operação == "multiplicação":
  print( n1 * n2)

#Se for escolhido divisão, o Pynthon divide n1 por n2 e mostra o resultado na tela.
elif operação == "divisão":
  print( n1 / n2)

 
