print("*******************************")
print("Bem vindo ao jogo de advinhacao")
print("*******************************")

import random

#gerando o número secreto que o usuário deverá advinhar
numero_secreto = random.randrange(1, 101)

#Capturando o número tentativa do usuário
tentativa = int(input("Digite um número: "))

acerto = tentativa == numero_secreto
abaixo = tentativa <  numero_secreto
acima  = tentativa >  numero_secreto

print("Você digitou o número: ", tentativa)

#verificando se o número digitado está acima, abaixo ou correto
if(acerto):
    print("Você acertou o número corretamente!!")

elif(abaixo):
    print("O número está ABAIXO!!")

elif(acima):
    print("O número está ACIMA!!")

print("FIM DO JOGO")