


saldo = 0
limite = 2000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10


def menu (): 
    menu = """
    ===================== MENU ===================== 
    [s] Sacar
    [d] Depositar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair
    [l] Limite diário utilizado
    => """
    return input(menu)

def listar_contas(contas): 
    for conta in contas:
        linha = f'''
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular

'''
        print ('=' + 100)
        print (linha)

def depositar (saldo, valor, extrato, /):
    if valor > 0: 
        saldo += valor 
        extrato += f"Depósito: R$ {valor:.2f}"
        print ('|||||||||||| Depósito realizado com sucesso! ||||||||||||')
    else: 
        print ('@@@@@@@@ Operação falhou! O valor informado é inválido. @@@@@@@@')
    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques): 
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite 
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo: 
        print ('@@@ Erro na operação! Saldo insuficiente. @@@')
    
    elif excedeu_limite: 
        print ('@@@ Erro na operação! Valor do saque acima do limite.@@@')
    
    elif excedeu_saques: 
        print ('@@@ Erro na operação! Limite de saques excedido. @@@')
    
    elif valor > 0: 
        saldo -= valor 
        extrato += f"Saque: R$ {valor:.2f}"
        numero_saques += 1 
        print ('=== Saque realizado com sucesso! ===')

    else: 
        print ('@@@ Erro na operação! O valor informado é inválido. @@@')


    return saldo, extrato 

def exibir_extrato(saldo, /, *, extrato): 
    print ('========================= EXTRATO =========================')
    print ('Não foram realizadas movimentações.' if not extrato else extrato)
    print (f'Saldo: R$ {saldo:.2f}')
    print ('===========================================================')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf] 
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios): 
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(usuario (cpf, usuarios))

    if usuario: 
        print ('@@@ Já existe usuário com esse CPF! @@@')
        return 

    nome = input ('Informe o nome completo: ')
    data_nascimento = input ('Informe a data de nascimento (dd-mm-aaa): ')
    endereco = input ('Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ')

    usuarios.append ({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print ('=== Usuário criado com sucesso! ===')

def criar_conta (agencia, numero_conta, usuarios): 
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    
def main (): 
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()