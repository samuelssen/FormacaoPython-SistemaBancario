

saldo = 0
limite = 2000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10

while True:
    menu = """

    [s] Sacar
    [d] Depositar
    [e] Extrato
    [q] Sair
    [l] Limite diário utilizado
    => """
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação realizada! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação não realizada! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação não realizada! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não realizada! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "l": 
        print (f'Você ainda tem {limite - valor} do seu limite diário para sacar.')

    elif opcao == "q":
        break    
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")