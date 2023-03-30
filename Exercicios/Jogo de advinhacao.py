print("*******************************")
print("Bem vindo ao jogo de advinhacao")
print("*******************************")

import random

#gerando o número secreto que o usuário deverá advinhar
numero_secreto = random.randrange(1, 101)

#Selecionando o nível de dificuldade do jogo.
print("Antes de começarmos o jogo, escolha um nível de dificuldade: ")
dificuldade = int(input("[1] = Fácil | [2] = Médio | [3] = Difícil \n"))

#Atribuindo o nível ao total de tentativas.
if(dificuldade == 1):
    total_de_tentativas = 10
elif(dificuldade == 2):
    total_de_tentativas = 5
else:
    total_de_tentativas = 3


#Loop parar iterar com a quantidade de tentativas de acordo com o nível escolhido.
for rodada in range(1, total_de_tentativas + 1):
    tentativa = int(input("Digite um número de 1 a 100: "))

    acerto = tentativa == numero_secreto
    abaixo = tentativa <  numero_secreto
    acima  = tentativa >  numero_secreto

    print("Você digitou o número: ", tentativa)

    #verificando se o número digitado está acima, abaixo ou correto.
    if(acerto):
        print("Você acertou o número corretamente!!")

    elif(abaixo):
        print("O número está ABAIXO!!")

    elif(acima):
        print("O número está ACIMA!!")

print("FIM DO JOGO, o número era: ", numero_secreto)