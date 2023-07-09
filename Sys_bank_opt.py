def menu():
    mm = f"""-=-=-=-=-=-=-=-=-=-Opções-=-=-=-=-=-=-=-=-=-    
[d] Depositar           [u] Criar Usúario
[s] Sacar               [l] Listar Usúario
[e] Extrato             [c] Criar Conta
[q] Sair                [m] Listar Contas
-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-
=> """
    return mm
def deposito(valordeposito, saldo, extrato):
    if valordeposito <= 0:
        print(linha)
        print(f'O valor R${valordeposito:.2f} é ZERO ou NEGATIVO,\n seu deposito não é VALIDO!')
        print(linha)

    else:
        saldo += valordeposito
        extrato += f'\nDeposito:      R$+{valordeposito:.2f}'
        print(linha)
        print(f'Seu Deposito foi realizado, no valor de R${valordeposito:.2f}')
        print('Desejamos a você um bom dia, volte sempre.')
        print(linha)

    return saldo, extrato
def saque(valorsaque, saldo, numero_saque, LIMITE_SAQUE, limite, extrato):
    if numero_saque == LIMITE_SAQUE:
        print('Infelizmente já foi realizado os 3 SAQUES diários.'
              '\nCaso ainda deseje sacar, vá a uma agência mais próxima de você. ')

    else:
        if valorsaque <= 0:
            print(linha)
            print(f'O valor R${valorsaque:.2f} é ZERO ou NEGATIVO,\n seu SAQUE não é VALIDO!')
            print(linha)

        elif valorsaque > saldo:
            print(linha)
            print(f'O valor R${valorsaque:.2f} é maior que o LIMITE de SALDO,'
                  f'\nSeu SALDO é de R$ {saldo:.2f}\nSeu LIMITE de saque è {limite:.2f}')
            print(linha)

        elif valorsaque > limite:
            print(linha)
            print(f'O valor R${valorsaque:.2f} é maior que o LIMITE de SAQUE,'
                  f'\n seu LIMITE de SAQUE é de R$ {limite:.2f}')
            print(linha)

        else:
            saldo -= valorsaque
            numero_saque += 1
            extrato += f'\nSaque:         R$-{valorsaque:.2f}'
            print(linha)
            print(f'O valor de R${valorsaque:.2f} foi sacado com sucesso!')
            print(f'Seu novo Saldo agora é de R${saldo:.2f}')
            print('Desejamos a você um bom dia, volte sempre.')
            print(linha)

    return saldo, numero_saque, extrato
def mostra_extrato(saldo, extrato):
    print(linha)
    print(extrato)
    print(f'Seu Saldo é de R$ {saldo:.2f} !')
    print('Desejamos a você um bom dia, volte sempre.')
    print(linha)
def creat_user(listacliente):
    cpf = input('Digite o valor do CPF(somente números): ')
    usuario = val_user(cpf, listacliente)

    if usuario is not None:
        print(linha)
        print('     já existe usúario com este CPF')
        print(linha)
        return

    else:
        nome = str(input('Nome: '))
        dt_nascimento = str(input('Data de Nascimento(DDMMYYYY): '))
        endereco = str(input('Endereço (logratura, nr - bairo - cidade/Sigla Estrado): '))
        listacliente.append({'nome': nome, 'dt_nascimento': dt_nascimento, 'cpf': cpf, 'endereco': endereco})
        print(linha)
        print('     Usúario criado com sucesso')
        print(linha)
def val_user(cpf, listacliente):
    rvalidador = None
    for i in listacliente:
        if i['cpf'] == cpf:
            rvalidador = i
    return rvalidador
def listallclientes(listacliente):
    for i in listacliente:
        print(linha)
        print(
            f'Nome : {i["nome"]}' + '\n'
            f'Data : {i["nome"]}' + '\n'
            f'CPF  : {i["cpf"]}' + '\n'
            f'Endereço : {i["cpf"]}')
        print(linha)
def creat_count(AGENCIA, n_count, listacliente):
    cpf = input('Digite o valor do CPF(somente números): ')
    cliente = val_user(cpf, listacliente)

    if cliente is None:
        print(linha)
        print('     Não existe usúario com este CPF')
        print(linha)
        return

    else:
        listaconta.append({'agencia': AGENCIA, 'numero_conta': n_count, 'cliente': cliente})
        print(linha)
        print(f'     Conta criada com sucesso!!! ')
        print(linha)
def listallcontas(listaconta):
    for k in listaconta:
        print(
        f'Agência  :     {k["agencia"]}' + '\n'
        f'Nª Conta :     {k["numero_conta"]}' + '\n'
        f'Nome Titular : {k["cliente"]["nome"]}')
        print(linha)


# Programa em execução
saldo = 0
limite = 500
extrato = str(' '*12+'Historico do EXTRATO')
numero_saque = 0
LIMITE_SAQUE = 3
AGENCIA = '0001'
linha = str('-='*11 + '=-'*11)
listacliente = []
listaconta = []
while True:
    opcao = input(menu())

    if opcao == 'd':
        print('Deposito')
        valordeposito = float(input('Digite o valor do DEPOSITO. R$ '))
        saldo, extrato = deposito(valordeposito, saldo, extrato)

    elif opcao == 's':
        print('Saque')
        valorsaque = float(input('Digite o valor do SAQUE. R$ '))
        saldo, numero_saque, extrato = saque(valorsaque =valorsaque, saldo=saldo, numero_saque=numero_saque,
                                             LIMITE_SAQUE=LIMITE_SAQUE, limite=limite, extrato=extrato)

    elif opcao == 'e':
        print('Extrato')
        mostra_extrato(saldo, extrato=extrato)

    elif opcao == 'u':
        print('Usúario')
        #listacliente = creat_user()
        creat_user(listacliente)

    elif opcao == 'c':
        n_count = len(listaconta) + 1
        print('Conta')
        creat_count(AGENCIA, n_count, listacliente)


    elif opcao == 'm':
        print('Lista de Contas(s)')
        listallcontas(listaconta)

    elif opcao == 'l':
        print('Lista de Usúario(s)')
        listallclientes(listacliente)

    elif opcao == 'q':
        break

    else:
        print('Operação INVÁLIDA, por favor selecione novamente a operação desejada.')
