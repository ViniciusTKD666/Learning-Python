def cria_conta(numero, titular, saldo, limite):
    conta = {"numero:": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return(conta)

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(saldo):
    print("Seu saldo atual é de: {}" .format(conta["saldo"]))

