#NUMERO PAR OU IMPAR

#Mostra uma mensagem para o usuário digitar um número e aguarda a resposta.
Número = int(input("Digite um número: "))

#Se o número digitado, ao ser dividido por 2, o resto da divisão for 0, aparecerá a mensagem dizendo que é par.
if Número % 2 == 0:
    print(f"O número {Número} é par.")

#Caso o o número não for divisível por 2, aparecerá a mensagem de que o número digitado é ímpar.
else:
    print(f"O número {Número} é ímpar.")
