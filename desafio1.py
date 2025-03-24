menu = """
-------------------------------
Banco UX
-------------------------------
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
-------------------------------
Selecione a operação desejada:
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
       valor = float(input("Informe o valor que deseja depositar: "))
       if valor > 0:
        saldo += valor
        extrato += f"Depósito: +R$ {valor:.2f}\n"
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")
       else: 
          print("Valor inválido! O saque deve ser maior que zero.")
    
    elif opcao == "2":

       valorSaque = float(input("Informe o valor que deseja sacar: "))

       if valorSaque > saldo:
          print("Saldo Insuficiente")

       elif valorSaque > limite:
          print("Valor acima do limite de saque diario.")

       elif numero_saques >= limite_saques:
          print("Quantidade de saques diarios atingiu o limite")

       elif valorSaque <= limite and numero_saques < limite_saques:
          saldo -= valorSaque
          numero_saques += 1
          extrato += f"Saque: -R$ {valorSaque:.2f}\n"
          print(f"Saque de R$ {valorSaque} realizado com sucesso!")

       else:
          print("Valor inválido! O saque deve ser maior que zero.")

    elif opcao == "3":
       print("-----Extrato-----")
       if not extrato:
          print("Nenhuma movimentação realizada.")
       else:
        print(extrato.strip())
        print(f"\nSaldo atual: R$ {saldo:.2f}")
    
    elif opcao == "4":
        print("Saindo... Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção inválida! Escolha uma opção entre 1 e 4.")
       
            