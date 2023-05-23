print("********************************")
print("***Bem-vindo ao jogo da forca***")
print("********************************")

palavraSecreta = "banana"
palavraEscondida = ["_","_","_","_","_","_"]

enforcou = False
acertou = False

while(not enforcou and not acertou):
    tentativa = input("Digite uma letra de A a Z: ")
    tentativa = tentativa.strip()

    index = 0

    for letraIterada in palavraSecreta:

        if(tentativa.upper() == letraIterada.upper()):
            palavraEscondida[index] = letraIterada

        index = index + 1
 
    print (palavraEscondida)


   # if(index == -1):

    #break;

print("Fim do jogo")
