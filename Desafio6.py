#Tempo

#Mostra a mensagem e espera o usuário digitar algo.
segundos = int(input("Digite a quantidade de segundos: "))

#Calcula quantas horas completas cabem no total de segundos, dividindo segundos por 3600, pois, 1 hora=3600 segundos.
horas = segundos // 3600

#Aqui, calcula quantos segundos sobram depois de tirar as horas completas.
resto = segundos % 3600

#Calcula qauntos minutos cabe no resto.
minutos = resto // 60

#Calcula quantos segundos ainda sobram depois dos minutos.
segundos_restantes = resto % 60

#Mostra na tela as horas, minutos e segundos calculados.
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_restantes)

#Nas 3 linhas seguintres, pergunta ao usuário as horas, minutos e segundos separadamente.
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

#Converte tudo para segundos.
Total segundos = horas * 3600 + minutos * 60 + segundos

#Mostra na tela o total de segundos calculado.
print("Total em segundos:", total_segundos)
