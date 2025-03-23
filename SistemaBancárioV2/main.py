# Importando bibliotecas
import time
import textwrap

#Função para menu.
def menu():
    menu = """\n========================
==  SISTEMA BANCÁRIO  ==
========================

Por favor, selecione a ação que deseja realizar.
[1]Cadastrar novo usuário.
[2]Cadastrar nova conta.
[3]Listar contas.
[4]Depósito.
[5]Saque.
[6]Extrato.
[0]Sair.
-> """
    # Retorna o menu e a entrada de dados.
    return input(textwrap.dedent(menu))

#Função para cadastrar usuários.
def cadastro_de_usuário(usuarios):
    # Entrada para o nome de usuário.
    nome = input("Insira seu nome: ")

    # Entrada para a data de nascimento do usuário.
    nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")

    # Entrada para o endereço do usuário.
    endereco = input("Informe seu endereço (Estado, Cidade, Bairro, Rua, Numero da casa): ")

    # Entrada para o CPF do usuário.
    cpf = input("Informe seu CPF (apenas números): ")

    # A variável usuário recebe o filtro de usuários.
    usuario = filtro_de_usuarios(cpf, usuarios)

    # Se o CPF que algum usuário digitou ja estiver cadastrado, o programa irá mostrar na tela que já existe um usuário cadastrado com o CPF digitado.
    if usuario:
        print("-" * 50)
        print(" - Já existe um usuário cadastrado com esse CPF! - ")
        print("-" * 50)
        return
    
    # Os valores que o usuário digitou serão adicionados em uma lista chamado "usuarios".
    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})

    # Se tudo correr bem uma mensagem de sucesso será impressa na tela.
    print("=" * 28)
    print("Usuário criado com sucesso!")
    print("=" * 28)

# Função para filtrar usuários.
def filtro_de_usuarios(cpf, usuarios):
    # A variável "usuarios_filtrados" recebe a verificação se algum CPF já foi digitado.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função para cadastrar contas.
def cadastro_de_conta(agencia, numero_conta, usuarios):
    # Entrada para o CPF do usuário.
    cpf = input("Informe seu CPF (Somente números): ")

    # A variável "usuario" recebe a função "filtro_de_usuarios" para verificar se de fato existe um usuário.
    usuario = filtro_de_usuarios(cpf, usuarios)

    # Se o usuário existir, a conta é criada e é mostrado na tela uma mensagem de sucesso.
    if usuario:
        print("=" * 27)
        print("Conta criada com sucesso!")
        print("=" * 27)
        # Retorna uma lista com os dados digitados pelo usuário.
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    # Se não é mostrado uma mensagem de erro.
    else:
        print("-" * 57)
        print(" - Usuário não encontrado. Por favor, tente novamente! - ")
        print("-" * 57)

# Função para listar contas.
def listar_contas(contas):
    # Estrutura condicional para identificar se existem contas cadastradas ou não.
    if len(contas) <= 0:
        print("Não existem contas cadastradas!")
    # É criado um laço de repetição, onde é passado todos os elementos da lista contas.
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Conta:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 50)
        print(textwrap.dedent(linha))
        print("=" * 50)

# Função para depósito.
def deposito(saldo, valor, extrato, /):
    # Se o valor for maior que 0, o valor deve ser somado na váriavel saldo e apresentar uma mensagem de sucesso.
    if valor > 0:
        saldo = saldo + valor
        print("=" * 40)
        print("Depósito realizado com sucesso!")
        print("=" *40)
        # O valor é atribuído na variável extrato com uma quebra de linha no final.
        extrato = extrato + f"Depósito: R$ {valor:.2f}\n"
        # Se não, é mostrado uma mensagem de erro.
    else:
        print("-" * 80)
        print("Houve uma falha na operação, valor informado inválido. Por favor, tente novamente!")
        print("-" * 80)
    # Retrona o saldo e o o extrato.
    return saldo, extrato

# Função para saque.
def saque(*, saldo, valor, extrato, limite, saques):
        # O valor do saque tem que ser maior que 0 e menor ou igual que R$500,oo.
        if valor > 0 and valor <= 500:
            # Tem que ser respeitado o limite diário de 3 saques.
            if saques < 3:
                """ Se as regras forem seguidas, o programa irá mostrar uma mensagem de sucesso e incrementar 1 a variável saque 
                e adicionar o valor do saque na variável extrato."""  
                if valor <= saldo:
                    saldo = saldo - valor
                    print("Saque realizado com sucesso!")
                    saques = saques + 1
                    extrato = extrato + f"Saque: R$ {valor:.2f}\n"
                         # M E N S A G E N S    D E    E R R O S
                else:
                    print("Operação falhou, saldo indisponível. Por favor, tente novamente!")
            else:
                print("Operação falhou, limite máximo de saques diários atingido. Por favor, tente novamnte amanhã!")
        else:
            print("Operação falhou, valor do saque inválido ou superior a R$500,00. Por favor, tente novamente!")
        # Retrona o saldo e o extrato.
        return saldo, extrato, saques  

# Função para extrato.
def mostrar_extrato(saldo, /, *, extrato):
    print("====================Extrato====================")
        # Se operações ainda não foram feitas, será impresso na tela.
    print("Não foram realizadas operações em sua conta." if not extrato else extrato)
        # Irá ser impresso na tela o saldo e as operações.
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=" * 47)

# Função principal.
def main():
    # Declarando variáveis.
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    saques = 0
    usuarios = []
    contas = []
    # Laço de repetição para manter o programa.
    while True:
        # A variável "opcao" recebe a função "menu".
        opcao = menu()

        # Opção para cadastro de usuários.
        if opcao == "1":
            cadastro_de_usuário(usuarios)
            time.sleep(2)

        # Opção para cadastro de contas.
        elif opcao == "2":
            numero_conta = len(contas) +1
            conta = cadastro_de_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            time.sleep(2)

        # Opção para listar de contas.
        elif opcao == "3":
            listar_contas(contas)
            time.sleep(2)

        # Opção para depósito.
        elif opcao == "4":
            valor = float(input("Informe o valor do depósito: R$"))
            saldo, extrato = deposito(saldo, valor, extrato)
            time.sleep(2)

        # Opção para saque.
        elif opcao == "5":
            valor = float(input("Informe o valor do saque: R$ "))       
            saldo, extrato, saques = saque( 
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                saques = saques,
            )
            time.sleep(2)

        # Opção de extrato.
        elif opcao == "6":
            mostrar_extrato(saldo, extrato = extrato)
            time.sleep(2)

        # Opção de sair.
        elif opcao == "0":
            print("Encerrado, obrigado!")
            time.sleep(2)
            break

        # Mensagem de erro caso o usuário digite um número que não é referente à nenhuma ação.
        else:
            print("Operação inválida. Por favor, tente novamente.")
            time.sleep(2)

main()