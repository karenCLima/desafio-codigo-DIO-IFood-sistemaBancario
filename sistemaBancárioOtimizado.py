def saque(*,saldo,numero_saques,extrato):
    if saldo <=0:
        return print("Saldo insuficiente! Não é possível realizar a operação!")
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
    return saldo, extrato, numero_saques

def deposito(saldo, extrato,/):
    deposito = float(input("Digite o valor do depósito: "))
       
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito no valor de R$ {deposito: .2f}.\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Erro na Operação.\n Não é possível depositor valores negativos!")
    return saldo, extrato
        
def extrato(saldo,/,*,extrato):
    if extrato !="":
        print("########## EXTRATO #############")
        print(extrato)
        print(f"Seu Saldo é de R$ {saldo:.2f}\n")
    else:
        print("Não foram realizadas movimentações. ")
        
def criar_usuario(lista):
    print("Vamos cadastrar um usuário.")
    cpf = input("Digite o CPF: ")
    cpf_numerico ="".join(num for num in cpf if num.isdigit())
    
    for usuario in lista:
        if(cpf_numerico == usuario["cpf"]):
            print("CPF já cadastrado!")
            return lista
    
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a sua data de nascimento: ")
    lougradouro = input("Digite seu lougradouro: ")
    nro = input("Digite o número: ")
    bairro = input("Digite o nome do seu bairro: ")
    cidade = input("Digite o nome da sua cidade: ")
    sigla_estado = input("Digite a sigla do seu estado: ")
        
    endereco = f"{lougradouro},{nro} - {bairro} - {cidade}/{sigla_estado}"
        
    usuario = {"cpf":cpf_numerico,"nome":nome, "data":data_nascimento, "endereco":endereco}
    lista.append(usuario)
    print("Usuário cadastrado com sucesso!")
    print(usuario)
    return lista
    
def  criar_conta(lista, lista_usuarios,cpf, numero_conta):
    agencia = "0001"
    num_conta = numero_conta;
    numero_conta += 1;
    for usuario in lista_usuarios:
        if cpf == usuario["cpf"]:
            nome = usuario["nome"]
            lista.append({"nome":nome, "agencia":agencia,"conta":num_conta})
            print("Conta criada com sucesso!")
            print({"nome":nome, "agencia":agencia,"conta":num_conta})
            return lista, numero_conta 
    print("CPF não cadastrado!")
    return lista, numero_conta 
     
    


extrato = ""
saldo = 0
numero_saques = 0
lista_usuarios = list();   
lista_contas = list();
numero_conta = 1;

while(True):
   opcao = int(input("""Escolha uma opção: \n
              1- Sacar\n
              2- Depositar\n
              3- Vizualizar extrato\n
              4- Criar usuário\n
              5- Criar conta\n
              6- Mostrar usuários\n
              7- Sair\n""")) 
   if opcao ==1:
       saldo, extrato, numero_saques = saque(saldo=saldo, numero_saques=numero_saques, extrato=extrato)
   elif opcao == 2:
       saldo, extrato = deposito(saldo,extrato)
   elif opcao == 3:
       extrato(saldo, extrato=extrato)
   elif opcao == 4:
       lista_usuarios = criar_usuario(lista_usuarios)
   elif opcao == 5:
       cpf = input("Digite o CPF: ")
       cpf_num ="".join(num for num in cpf if num.isdigit())
       lista_contas,numero_conta = criar_conta(lista_contas,lista_usuarios,cpf_num,numero_conta)
   elif opcao == 6:
       for usuario in lista_usuarios:
           print(usuario)
           print("")
   elif opcao ==7:
       print("Saindo do sistema!")
       break
   else:
       print("Opção inválida! Escolha uma das opções válidas.")
           
       
       


    