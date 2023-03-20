print("*******************************")
print("Bem vindo ao jogo de advinhacao")
print("*******************************")

numero_secreto = 31

tentativa = int(input("Digite um número: "))

acerto = tentativa == numero_secreto
abaixo = tentativa <  numero_secreto
acima  = tentativa >  numero_secreto

print("Você digitou o número: ", tentativa)

if(acerto):
    print("Você acertou o número corretamente!!")

elif(abaixo):
    print("O número está ABAIXO!!")

elif(acima):
    print("O número está ACIMA!!")

print("FIM DO JOGO")