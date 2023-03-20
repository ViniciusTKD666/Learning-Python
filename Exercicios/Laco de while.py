print("*******************************")
print("Bem vindo ao jogo de advinhacao")
print("*******************************")

numero_secreto = 31
TotalDeTentativas = 5
TentativaAtual = 1




    
while(TentativaAtual <= TotalDeTentativas):
    tentativa = int(input("Digite um número: "))

    acerto = tentativa == numero_secreto
    abaixo = tentativa <  numero_secreto
    acima  = tentativa >  numero_secreto

    print("Você digitou o número: ", tentativa)

    if(acerto):
        print("Você acertou o número corretamente!! na tentativa {} de {}".format(TentativaAtual, TotalDeTentativas))
        break

    elif(abaixo):
        print("O número está ABAIXO!!, tentativa: {} de {}".format(TentativaAtual, TotalDeTentativas))

    elif(acima):
        print("O número está ACIMA!!, tentativa: {} de {}".format(TentativaAtual, TotalDeTentativas))

    TentativaAtual = TentativaAtual+1 

print("FIM DO JOGO")
