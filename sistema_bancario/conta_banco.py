"""
DESAFIO DE CODIGO DIO
HELDER LOPES AGO/2023
"""

menu = """
    Digite uma opção:
    [d] Deposito
    [s] Saque
    [e] Extrato
    [q] Sair
    => \n"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
depositos = []

while True:
    opcao = input(menu)

    """funcao deposito declarada dentro do while para que o mesmo so sera usado
    em tempo de execução do laço.
    é passado o parametro saldo para que a função atribui localmente o valor
    global evitando erro de calculo com none"""

    # FUNCAO DE DEPOSITO
    def deposito(saldo, depositos):
        print(f"Saldo  atual {saldo}")
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"\nDeposito de R$ {saldo:.2f} realizado com sucesso. ")
            depositos.append(valor_deposito)

        return saldo, depositos

    # FUNCAO DE SAQUE
    def saque(saldo):
        while True:
            valor_saque = 0.00
            print(f"Saldo em conta R$ {saldo}")

            if valor_saque < 500:
                if saldo <= 0.00:
                    print(
                        f"Saque indisponível. Desculpe, sua conta está SEM SALDO. R$ {saldo:.2f}"
                    )
                    return

                elif saldo > valor_saque:
                    valor_saque = float(
                        input("Digite o valor que quer retirar ou 0 para retornar")
                    )
                    if valor_saque != 0:
                        if saldo < valor_saque:
                            print(
                                f"Digite um valor maior que seu saldo. Seu saldo é R$ {saldo:.2f}"
                            )
                        else:
                            saldo = saldo - valor_saque
                            depositos.append(-valor_saque)
                            print(f"Retire seu dinhero. R$ {valor_saque:.2f} ")

                            # corrigir este else pois quando o valor é inferior ao saldo ele entra no laço mas não mostra nada ate ser satisfeita a condição de diferent ede - e maior que o saldo

            else:
                print(
                    "Voce alcançou o limite de depoisto diário. Tente amanhã ou procure atendimento no guichês"
                )
            if valor_saque == 0:
                break
        return

    # EXTRATO
    def extrato(depositos):
        sair = "s"

        while sair == "s":
            sair = input("Deseja exibir o extrato? [s]im ou [n]ao?")
        return

        print("Erro de impressao")

    # MENU
    if opcao == "d" or opcao == "D":
        print("Depósito")
        # é necessario atribuir ao retorno da função as variaveis que quero armazenar. no caso o saldo e o   historico de movimentações
        saldo, depositos = deposito(saldo, depositos)

        print(f"seu saldo fora é {saldo}")

    elif opcao == "s" or opcao == "S":
        print("Saque")
        saque(saldo)

    elif opcao == "e" or opcao == "E":
        print(f"Extrato {depositos}")

    elif opcao == "q" or opcao == "Q":
        break

    else:
        print("Operação inválida, por favor digite uma opção")
