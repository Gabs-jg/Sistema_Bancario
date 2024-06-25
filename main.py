# Projeto de Sistema Bancário.

# Importando bibliotecas:
import time

# Definindo uma váriavel contendo o menu dentro para simplificar o código:
menu = """\n========================
==  SISTEMA BANCÁRIO  ==
========================

Por favor, selecione a ação que deseja realizar.
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
-> """

# Definindo variáveis:
saldo = 0
saques = 0
limite = 500
extrato = ""

# Criando um laço de repetição onde é definido que a condição sempre será verdadeira:
while True:

    # Atribui à variável "opcao" o número da ação que escolhemos.
    # O menu sempre será mostrado pois o mesmo está dentro do input que está no laço de repetição onde a condição sempre sera verdadeira.
    opcao = input(menu)

    # Opção de depósito:
    if opcao == "1":
        # O usuário irá digitar o valor de depósito, onde o valor tem que ser maior que 0.
        valor = float(input("Por favor, digite o valor do depósito: R$"))
        if valor > 0:
            # Se o valor for maior que 0, o valor deve ser somado na váriavel saldo.
            saldo = saldo + valor
            # O valor é atribuído na variável extrato com uma quebra de linha no final.
            extrato = extrato + f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Houve uma falha na operação, valor informado inválido. Por favor, tente novamente!")

    # Opção de Saque:
    elif opcao == "2":
        # O usuário irá digitar o valor do saque. Para osaque ser efetuado é preciso seguir algumas regras.
        valorSaque = float(input("Por favor, digite o valor do saque: R$"))
        # O valor do saque tem que ser maior que 0 e menor ou igual que R$500,oo.
        if valorSaque > 0 and valorSaque <= 500:
            # Tem que ser respeitado o limite diário de 3 saques.
            if saques < 3:
                """ Se as regras forem seguidas, o programa irá mostrar uma mensagem de sucesso e incrementar 1 a variável saque 
                e adicionar o valor do saque na variável extrato."""  
                if valorSaque <= saldo:
                    saldo = saldo - valorSaque
                    print("Saque realizado com sucesso!")
                    saques = saques + 1
                    extrato = extrato + f"Saque: R$ {valorSaque:.2f}\n"
                else:
                    print("Operação falhou, saldo indisponível. Por favor, tente novamente!")
            else:
                print("Operação falhou, limite máximo de saques diários atingido. Por favor, tente novamnte amanhã!")
        else:
            print("Operação falhou, valor do saque inválido ou superior a R$500,00. Por favor, tente novamente!")

    # Opção de extrato:
    elif opcao == "3":
        print("==========Extrato==========")
        # Se operações ainda não foram feitas, será impresso na tela.
        print("Não foram realizadas operações em sua conta." if not extrato else extrato)
        # Irá ser impresso na tela o saldo e as operações.
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================")

    # Opção de saída:    
    elif opcao == "0":
        # É mostrado na tela um agradecimento e após 5 segundos o programa é encerrado.
        print("Obrigado!")
        time.sleep(5)
        break

    # Caso o usuário digite um número que não é referente a nenhuma ação, o programa apresentará erro.
    else:
        print("Opção inválida, tente novamente.")


