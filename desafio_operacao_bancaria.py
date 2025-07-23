saldo = 0
LIMITE_SAQUE = 3
VALOR_LIMITE_SAQUE = 500
extrato = ""
numero_saques = 0


while True:
    menu = """
        Selecione a opção desejada:

        [1] - Saldo atual
        [2] - Depósito
        [3] - Saque
        [4] - Extrato
        [5] - Sair
    """
    print(menu)
    opcao = int(input("Digite a opção desejada: "))

    print(opcao)
    if opcao == 1:
        print(f"Saldo atual: R$ {saldo:4.2f}")

    elif opcao == 2:
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            extrato += f"Depósito: R$ {valor_deposito: .2f}\n"

            print("Depósito efetuado com sucesso!")
            print(f"Saldo atual: R$ {saldo: 4.2f}")

        else:
            print("Digite um valor válido!")

    elif opcao == 3:

        valor_saque = float(input("Digite o valor a ser sacado: "))

        if valor_saque > saldo:
            print("Saldo insuficiente. Tente outro valor!!")

        elif valor_saque > VALOR_LIMITE_SAQUE:
            print(f"O valor do saque excede o limite de R$ {VALOR_LIMITE_SAQUE: .2f} por operação.")

        elif numero_saques >= LIMITE_SAQUE:
            print("Você excedeu o número máximo de saques diários. Tente novamente amanhã.")

        elif valor_saque > 0:
            print("Saque realizado com sucesso!!")
            saldo = saldo - valor_saque
            print(f"Saldo atual: R$ {saldo: 4.2f}")
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1

        else:
            print("A operação falhou. Digite um valor válido!\n")

    elif opcao == 4:
        print("\n============EXTRATO============")
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================")


    elif opcao == 5:
        break

    else:
        print(("Operação inválida. Selecione uma opção válida!"))

