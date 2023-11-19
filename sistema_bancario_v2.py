menu = '''
[D] Depósito       [CU] Cadastrar Usuário
[S] Saque          [BU] Buscar Usuário
[E] Extrato        [CC] Cadastrar Conta Corrente
[Q] Sair           [BC] Buscar Contas

'''
saldo = 0
qtd_saques = 0
limite = 500
LIMITE_SAQUES = 3
extrato = ''
usuarios = [{"cpf":'02518026398',"nome":'Gessione Sena', "data_nasc":'14/06/1986',"endereco":'Cajueiro do Boi'}]
contas = []
#**********Função para depósito**********************************
def depositar(valor_deposito,saldo_total,/):#argumentos chamados apenas por posição
    saldo_atual = saldo_total + valor_deposito
    
    return saldo_atual
#****************************************************************
#**********Função para saque************************************
def sacar(*,valor_saque,saldo_total):#argumentos chamados apenas por nomes
    saldo_atual = saldo_total - valor_saque
    
    return saldo_atual    
#****************************************************************
#**********Função para extrato**********************************
def mostrar_extrato(movimentacao,/,*,saldo_total):#argumentos chamados por nome e posição
    if extrato == '':
        #saida = (f"\n{f'Sem movimentação':>31}" if extrato == '' else movimentacao)
        saida = f"{f'Sem movimentação':>31}\n{'_'*31}\n{f'Saldo: R$ {saldo_total:.2f}  ':>31}\n"
    else:
        saida = f"{movimentacao}\n{'_'*31}\n{f'Saldo: R$ {saldo_total:.2f}  ':>31}\n"
    
    return saida
#****************************************************************
#**********Função criar usuario**********************************
def criar_usuario(usuarios,cpf): 
    teste = False
    for usuario in usuarios:
        item = usuario['cpf']
        if item == cpf: 
            teste = True
    if teste == False:    
        nome = input('Nome completo: ')
        data_nasc = input('Data de Nascimento: ')
        endereco = input('Endereço completo: ')
        dados_usuario = dict({"cpf":cpf,"nome":nome, "data_nasc":data_nasc,"endereco":endereco})
        
    return dados_usuario if teste == False else f'O CPF {cpf} já existe na base de dados!'
#****************************************************************
#**********Função buscar usuario**********************************
def buscar_usuario(usuarios,cpf): 
    teste = False
    for usuario in usuarios:
        item = usuario['cpf']
        if item == cpf: 
            teste = True
            resultado = usuario 
           
    return resultado if teste == True else f'O CPF {cpf} não existe na base de dados!'
#****************************************************************
#**********Função criar conta**********************************
def abrir_conta(usuarios,contas,cpf):
    teste = False
    for usuario in usuarios:
        item = usuario['cpf']
        if item == cpf:
            teste = True
    if teste == True:
        AGENCIA = '0001'
        conta_corrente = len(contas) + 1
        saldo = 0
        dados_conta = dict({'conta':conta_corrente,'agencia':AGENCIA, 'usuario':cpf, 'saldo':saldo})  
    return dados_conta if teste == True else f'Usuário {cpf} não existe no banco de dados!'
#****************************************************************
#**********Função listar contas**********************************
def buscar_contas(contas,cpf):
    list = []
    for conta in contas:
        item = conta['usuario']
        if cpf == item:
            list.append(conta)
    return f'Não há contas vinculadas ao CPF informado!' if list == [] else list
    
#****************************************************************
while True:
    opcao = input(menu).upper()
    
    #MÓDULO DEPÓSITO
    if opcao == 'D':
        cpf_usuario = input("Digite o CPF do titular da conta: ").strip()   
        busca = buscar_usuario(usuarios,cpf_usuario)#buscando usuario no banco de dados
        
        if isinstance(busca,dict):#caso o usuario exista, é hora de verificar se possui conta aberta
            search = buscar_contas(contas,cpf_usuario)
            if isinstance(search,list):#se a saida da função search for uma lista, isso quer dizer que há conta para o usuario buscado
                print(f"Contas vinculadas ao CPF {cpf_usuario}:\n{'_'*20}")
                for item in search:#iterando todas as contas vinculadas ao usuario
                    print(f"Agência: {item['agencia']}\nConta Nº: {item['conta']}\nSaldo: {item['saldo']:.2f}\n{'-'*20}")
                if len(search) == 1:#se usuario possuir apenas 1 conta
                    valor = float(input('Digite o valor a ser depositado: '))
                    if valor > 0:
                        for item in search:
                            item['saldo'] = depositar(valor,saldo)#atualizando a variavel saldo com o retorno da função depositar
                        #saldo = depositar(valor,saldo)#atualizando a variavel saldo com o retorno da função depositar 
                        extrato = f"{extrato}\n {f'R$ {valor:.2f} C':>30}"
                        print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")
                        
                    else:
                        print('Valor incorreto. Tente outro valor!')
                else:#caso possua mais de uma conta, deverá escolher
                    while True:#laço para a escolha da conta até um numero de conta valido ser digitado
                        escolha_conta = int(input('Qual conta deseja depositar? Digite o N° da conta: '))
                        
                        for item in search:
                            teste = False #teste para caso o numero digitado não coincida com nenhuma conta do usuario
                            if escolha_conta == item['conta']:
                                teste = True
                                valor = float(input('Digite o valor a ser depositado: '))
                                if valor > 0:
                                    item['saldo'] = depositar(valor,saldo)#atualizando a variavel saldo com o retorno da função depositar
                                    extrato = f"{extrato}\n {f'R$ {valor:.2f} C':>30}"
                                    print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")
                                else:
                                    print('Valor incorreto. Tente outro valor!')
                        
                        if teste == True:
                            break #parada do laço while
                        else:
                            print(f"Conta digitada não coincide com nenhuma conta vinculada ao usuário {busca['nome']}")
            else:
                print(search)
        else:
            print(busca)
    
    #MÓDULO SAQUE
    elif opcao == 'S':
        valor = float(input('Digite o valor a ser sacado:'))
        lim_valor_excedido = valor > limite
        lim_saque_excedido = qtd_saques >= LIMITE_SAQUES
        if valor <= 0:
            print('Valor Incorreto. Tente outro valor!')
        else:
            if lim_valor_excedido:
                print('Limite de valor diário excedido!')
            elif lim_saque_excedido:
                print('Limite de saque diário excedido!')
            elif valor <= saldo:
                saldo = sacar(valor_saque = valor,saldo_total = saldo)#atualizando a variavel saldo com o retorno da função sacar com argumentos passados apenas por nomes
                qtd_saques += 1
                extrato = f"{extrato}\n {f'R$ {valor:.2f} D':>30}"
                print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
                    
            elif saldo <= 0:
                print('Saldo Insuficiente!')

    #MÓDULO EXTRATO
    elif opcao == 'E':
        
        print(f"{'*'*31}\n{'E X T R A T O':^31}\n{'_'*31}")
        print(mostrar_extrato(extrato,saldo_total=saldo))#chamando função mostrarextrato() com argumentos posicionais e nominais
        print(f"{'*' *31}")  
    
    elif opcao == 'C':
        cpf_usuario = input('Digite o CPF do usuário: ').strip()

        novo_usuario = criar_usuario(usuarios,cpf_usuario)
        usuarios.append(novo_usuario) if isinstance(novo_usuario,dict) else print(novo_usuario)#caso a saida da função seja um dicionario, adiciona a lista usuarios, caso contrario, imprime uma mensagem
        if isinstance(novo_usuario,dict):#se a variavel novo_usuario é um dicionario
            print(f"Usuário {novo_usuario['nome']} foi cadastrado com sucesso!")
        
        print(usuarios)
    
    elif opcao == 'B':
        cpf_usuario = input("Informe o CPF: ").strip()
        search = buscar_usuario(usuarios,cpf_usuario)
        print(search)

    elif opcao == 'CC':
        cpf_usuario = input("Iremos abrir sua conta corrente. Informe o CPF: ").strip()
        
        nova_conta = abrir_conta(usuarios,contas,cpf_usuario)
        contas.append(nova_conta) if isinstance(nova_conta,dict) else print(nova_conta)

        if isinstance(nova_conta, dict):#se a variavel nova_conta é um dicionario
            print(f"Conta Corrente Nº {nova_conta['conta']}, Ag: {nova_conta['agencia']} cadastrada com sucesso! ")
        
    elif opcao == 'BC':

        while True:#laço para validar o cpf
            cpf_usuario = input("Buscar contas vinculadas ao CPF: ").strip()
            if len(cpf_usuario) == 11:
                break
            else:
                print('Digite um CPF válido:' )
        
        contas_por_cpf = buscar_contas(contas,cpf_usuario)#adiciona à variavel todas as contas vinculadas ao cpf caso possua
        if isinstance(contas_por_cpf,list):#se a variavel contas_por_cpf for uma lista
            print(f"Contas vinculadas ao CPF {cpf_usuario}:\n{'_'*20}")
            for item in contas_por_cpf:
                print(f"Agência: {item['agencia']}\nConta Nº: {item['conta']}\n{'-'*20}")
        else:
            print(contas_por_cpf)#imprime uma mensagem

        

    #SAIR
    elif opcao == 'Q':
          break
    
    else:
        print('Opção inválida. Escolha outra opção!')
