import textwrap

def menu():
    menu = """\n
-------------------------------
Banco UX
-------------------------------
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNova Conta
[5]\tListar contas
[6]\tNovo usuário
[7]\tSair
-------------------------------
Selecione a operação desejada:
"""
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: +R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! O depósito deve ser maior que zero.")

    return saldo, extrato


def sacar(*, saldo, valorSaque, extrato, limite, numero_saques, limite_saques):
    if valorSaque > saldo:
        print("Saldo Insuficiente")

    elif valorSaque > limite:
        print("Valor acima do limite de saque diário.")

    elif numero_saques >= limite_saques:
        print("Quantidade de saques diários atingiu o limite")

    elif valorSaque > 0:
        saldo -= valorSaque
        numero_saques += 1
        extrato += f"Saque: -R$ {valorSaque:.2f}\n"
        print(f"Saque de R$ {valorSaque:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! O saque deve ser maior que zero.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("----- Extrato -----")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        print(extrato.strip())
    print(f"\nSaldo atual: R$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nUsuário existente no sistema.")
        return

    nome = input("Informe seu nome completo: ")
    data_de_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite seu CEP: ")

    usuarios.append({
        "nome": nome,
        "data_de_nascimento": data_de_nascimento,
        "endereco": endereco,
        "cpf": cpf 
    })

    print("\nUsuário cadastrado com sucesso!")


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado. Crie o usuário primeiro. @@@")
    return None


def listar_contas(contas):
    
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    for conta in contas:
        linha = f""" 
        Agência:\t{conta['agencia']}
        C/c:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    agencia = "0001"

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valorSaque = float(input("Informe o valor que deseja sacar: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valorSaque=valorSaque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "7":
            print("Saindo... Obrigado por utilizar nosso sistema!")
            break

        else:
            print("Opção inválida! Escolha uma opção entre 1 e 7.")


main()
