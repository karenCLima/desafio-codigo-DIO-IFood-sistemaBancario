opcao = int(input("""Escolha uma opção: \n
              1 - Depositar\n
              2- Sacar\n
              3- Vizualizar extrato\n
              4- Sair\n"""))

extrato = ""
saldo = 0
numero_saques = 0

while opcao != 4:
    if opcao == 1:
       deposito = float(input("Digite o valor do depósito: "))
       
       if deposito > 0:
            saldo += deposito
            extrato += f"Depósito no valor de R$ {deposito: .2f}.\n"
            print("Depósito realizado com sucesso!")
       else:
           print("Erro na Operação.\n Não é possível depositor valores negativos!")
    elif opcao == 2:
        if saldo <=0:
            print("Saldo insuficiente! Não é possível realizar a operação!")
        else:
            if numero_saques <3:
                saque = float(input("Digite o valor que deseja sacar: "))
                
                if saque > saldo:
                    print("Não é possivel realizar a operação. Saldo insuficiente!")
                elif saque <= 0:
                    print("Não é possível sacar valores negativos ou nulos.")
                else:
                    if saque <= 500:
                        saldo -= saque
                        extrato += f"Saque no valor de {saque: .2f}\n"
                        numero_saques += 1
                        print("Saque realizado com sucesso!")
                    else:
                        print("Erro na operação. Valor do saque não pode exceder R$ 500,00.")
            else:
                print("Não é possível realizar mais do que 3 saques por dia!")
    elif opcao == 3:
        print(extrato)
        print(f"Seu Saldo é de R$ {saldo:.2f}\n")
    
    opcao = int(input("""Escolha uma opção: \n
              1 - Depositar\n
              2- Sacar\n
              3- Vizualizar extrato\n
              4- Sair\n"""))
                    
        
