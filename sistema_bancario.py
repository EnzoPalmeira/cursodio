menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 600
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado é inválido, tente novamente.")
        
   
    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_limite_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("O valor do saque excede o limite por saque.")
        elif excedeu_limite_saque:
            print("Número máximo de saques excedido.")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque:    R$ {valor_saque:.2f}\n"
            numero_saques += 1
        else:
            print("O valor informado é inválido.")
    

    elif opcao == "e":
        print("\n======= EXTRATO =======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo:   R$ {saldo:.2f}")
        print("========================\n")
    
    
    elif opcao == "q":
        print("Obrigado pela preferência. Encerrando...")
        break            

    else:
        print("Selecione uma opção válida.")
