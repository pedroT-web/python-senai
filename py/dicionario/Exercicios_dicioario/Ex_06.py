# Crie um dicionário para armazenar informações sobre contas
# bancárias. Cada conta deve ter número da conta, saldo e nome do
# titular. Permita que o usuário:
# - Consulte o saldo de uma conta;
# - Deposite dinheiro em uma conta;
# - Saque dinheiro de uma conta;
# - Transfira dinheiro entre contas.
contas_bancarias = {
    "365271": {"titular":"Café", "saldo": 391},
    "229833": {"titular": "Pedro", "saldo": 20},
    "398271": {"titular": "Gabriel", "saldo": 3928}
    
}
fazer = 0
continuar = "sim"
while continuar == "sim":
    conta = input("Digite o número da conta: ")
    fazer = int(input("""Digite o que deseja fazer: 
        1 - Consultar o saldo da conta.
        2 - Depositar dinheiro na conta.
        3 - Sacar dinheiro da conta.
        4 - Transferir dinheiro para outra conta.)
    """))
    saldo = contas_bancarias[conta]["saldo"]
    
    if fazer == 1:
        print("O saldo atual da conta é: R$", saldo)
    elif fazer == 2:
        deposito = float(input("Qual o valor que deseja depositar: "))
        saldo_novo = contas_bancarias[conta]["saldo"] = saldo + deposito
        
        print(f"Agora o saldo atual da conta {conta} é: {saldo_novo}")
    elif fazer == 3:
        saque = float(input("Quanto deseja sacar: "))
        saldo_novo = contas_bancarias[conta]["saldo"] = saldo - saque
        
        print(f"Agora o saldo atual da conta {conta} é: {saldo_novo}")
    elif fazer == 4:
        conta_destino = input("Digite o número da conta para qual deseja fazer a transferencia: ")
        valor_transferencia = float(input("Digite o valor da tranferencia: "))
        saldo_novo = contas_bancarias[conta]["saldo"] = saldo - valor_transferencia
        print(f"Saldo atual da conta {conta} é: R$ {saldo_novo}")
        
        # Outra conta
        saldo_conta_destino = contas_bancarias[conta_destino]["saldo"]
        saldo_novo_conta_destino = contas_bancarias[conta_destino]["saldo"] = saldo_conta_destino + valor_transferencia
        
        print(f"Saldo atual da conta {conta} é: R$ {saldo_novo_conta_destino}")
    else:
        print("Ação Incorreta, por favor insira uma ação correta")
    
    continuar = input("Deseja realizar outra ação? (sim ou não): ")
    
print("Ações Finalizadas!!")