#Calculadora simples
n1 = float(input("selecione um número: "))
n2 = float(input("selecione outro número: "))
operação = input("escolha uma operação [soma, subtração, multiplicação ou divisão]: ")
if operação == "soma":
  print( n1 + n2)
elif operação == "subtração":
  print( n1 - n2)
elif operação == "multiplicação":
  print( n1 * n2)
elif operação == "divisão":
  print( n1 / n2)
else:
  print("essa operação não existe")
 
 
