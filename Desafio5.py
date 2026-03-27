#Calcular área do triângulo

#As 2 próximas linhas perguntam qual é o valor da base e altura do triangulo e agurdará a resposta.
base = float(input("qual a base de seu triângulo:"))
altura = float(input("qual a altura de seu triângulo:"))

#Ao receber os dois valores, será feita a multiplicação da base e altura e depois será dividido por 2.
area = (base * altura) / 2

#Ao receber o resultado, será mostrado na tela.
print("A área do triângulo é:", area)
