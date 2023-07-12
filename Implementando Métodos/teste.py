def cria_conta(numero, titular, saldo, limite): # Define a função cria_conta, que recebe como argumento, numero, titular, saldo e limite
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite} # Cria o dicionário conta com os argumentos da função
    return conta # Retorna o dicionário


def deposita(conta, valor): # Define a função deposita, que recebe como argumento, conta e o valor
    conta["saldo"] += valor # Adiciona o valor ao saldo da conta

def saca(conta, valor): # Define a função saca, que recebe como argumento, conta e o valor
    conta["saldo"] -= valor # Subtrai o valor do saldo da conta

def extrato(conta): # Define a função extrato, que recebe como argumento a conta
    print("Saldo é {}".format(conta["saldo"])) # Imprime o seu saldo