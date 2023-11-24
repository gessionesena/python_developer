menu = '''
[D] Depósito       [C] Cadastrar Usuário
[S] Saque          [BU] Buscar Usuário
[E] Extrato        [CC] Cadastrar Conta Corrente
[Q] Sair           [BC] Buscar Contas

'''

limite = 500
LIMITE_SAQUES = 3
extrato = []
usuarios = []#{"cpf":'02518026398',"nome":'Gessione Sena', "data_nasc":'14/06/1986',"endereco":'Cajueiro do Boi'}
contas = []#{'conta':1,'agencia':'0001', 'usuario':'02518026398', 'saldo':0,'qtd_saques_diario':0}
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
def mostrar_extrato(num_conta,contas,extrato): 
    for item in contas:
        if item['conta'] == num_conta:
            print(f"Conta Nº: {num_conta}\nAgência: 0001\n{'-' *31}")
    for item in extrato:
        if item['conta'] == num_conta:
            print(f"{item['movimento']}")
    print(f"{'-' *31}")
    for item in contas:
        if item['conta'] == num_conta:
            print(f"Saldo: R$ {item['saldo']:.2f}")
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
    teste_busca = False
    for usuario in usuarios:
        item = usuario['cpf']
        if item == cpf: 
            teste_busca = True
            resultado = usuario 
           
    return resultado if teste_busca == True else f'O CPF {cpf} não existe na base de dados!'
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
        qtd_saques_diario = 0
        dados_conta = dict({'conta':conta_corrente,'agencia':AGENCIA, 'usuario':cpf, 'saldo':saldo,'qtd_saques_diario':qtd_saques_diario})  
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
#**********Função validar cpf**********************************
def valida_cpf(cpf):
    cpf = cpf.strip()#removendo espaços em branco
    if cpf.isdigit() and len(cpf) == 11:
        return True
    else:
        return False    
#****************************************************************

while True:
    opcao = input(menu).upper()
    
#MÓDULO DEPÓSITO
    if opcao == 'D':
        while True:
            cpf_usuario = input("Digite o CPF do titular da conta: ").strip() 
            validador = valida_cpf(cpf_usuario)
            if validador == True:
                break
            else:
                print('Digite um CPF válido!')

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
                        saldo_atual = search[0]['saldo']
                        saldo_atual = depositar(valor,saldo_atual)
                        search[0]['saldo'] = saldo_atual
                        
                        movimentacao = f"{f'{valor:.2f} C':>30}\n"
                        num_conta = search[0]['conta']
                        
                        if extrato != []:
                            teste_extrato = False
                            for item in extrato:
                                if num_conta == item['conta']:
                                    item['movimento'] = item['movimento'] + movimentacao#concatenando 
                                    teste_extrato = True 
                            if teste_extrato != True:
                                extrato.append(dict({'conta':num_conta, 'movimento':movimentacao}))            
                        else:
                            extrato.append(dict({'conta':num_conta, 'movimento':movimentacao}))  
                        print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")
                        
                    else:
                        print('Valor incorreto. Tente outro valor!')
                else:#caso possua mais de uma conta, deverá escolher
                    while True:#laço para a escolha da conta até um numero de conta valido ser digitado
                        escolha_conta = int(input('Qual conta deseja depositar? Digite o N° da conta: '))
                        teste_while = False #teste para caso o numero digitado não coincida com nenhuma conta do usuario
                        for item in search:
                            
                            if item['conta'] == escolha_conta:
                                teste_while = True
                                valor = float(input('Digite o valor a ser depositado: '))
                                if valor > 0:
                                    saldo_atual = item['saldo']
                                    saldo_atual = depositar(valor, saldo_atual)#atualizando a variavel saldo com o retorno da função depositar
                                    item['saldo'] = saldo_atual

                                    movimentacao = f"{f'{valor:.2f} C':>30}\n"
                                    if extrato != []:
                                        teste_extrato = False
                                        for item in extrato:
                                            if escolha_conta == item['conta']:
                                                item['movimento'] = item['movimento'] + movimentacao#concatenando 
                                                teste_extrato = True 
                                        if teste_extrato != True:
                                           extrato.append(dict({'conta':escolha_conta, 'movimento':movimentacao}))            
                                    else:
                                        extrato.append(dict({'conta':escolha_conta, 'movimento':movimentacao})) 

                                    print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")
                                    
                                else:
                                    print('Valor incorreto. Tente outro valor!')
                            
                        if teste_while == True:
                            break #parada do laço while
                        else:
                            print(f"Conta digitada não coincide com nenhuma conta vinculada ao usuário {busca['nome']}")
            else:
                print(search)#Não há contas vinculadas ao CPF informado!
        else:
            print(busca)#O CPF () não existe na base de dados!
    
#MÓDULO SAQUE
    elif opcao == 'S':
        #validando cpf
        while True:
            cpf_usuario = input("Digite o CPF do titular da conta: ").strip() 
            validador = valida_cpf(cpf_usuario)
            if validador == True:
                break
            else:
                print('Digite um CPF válido!')
        #buscando usuario no cadastro
        busca = buscar_usuario(usuarios,cpf_usuario)
        
        if isinstance(busca,dict):#caso o usuario exista, é hora de verificar se possui conta aberta
            search = buscar_contas(contas,cpf_usuario)
            if isinstance(search,list):#se a saida da função search for uma lista, isso quer dizer que há conta para o usuario buscado
                print(f"Contas vinculadas ao CPF {cpf_usuario}:\n{'_'*20}")
                for item in search:#iterando todas as contas vinculadas ao usuario
                    print(f"Agência: {item['agencia']}\nConta Nº: {item['conta']}\nSaldo: {item['saldo']:.2f}\n{'-'*20}")
                    

                if len(search) == 1:#se usuario possuir apenas 1 conta
                    valor = float(input('Digite o valor a ser sacado: '))
                    lim_valor_excedido = valor > limite
                    lim_saque_excedido = search[0]['qtd_saques_diario'] >= LIMITE_SAQUES
                    if valor <= 0:
                        print('Valor Incorreto. Tente outro valor!')
                    elif lim_valor_excedido:
                        print('Limite de valor diário excedido!')  
                    elif lim_saque_excedido:
                        print('Limite de saque diário excedido!')
                    elif valor <= search[0]['saldo']:
                        saldo_atual = search[0]['saldo']
                        saldo_atual = sacar(valor_saque = valor,saldo_total=saldo_atual) #atualizando a variavel saldo_atual com o retorno da função sacar com argumentos passados apenas por nomes 
                        search[0]['saldo'] = saldo_atual
                        search[0]['qtd_saques_diario'] += 1 #atualizando a qtd_saques_diario da conta em questão
                        
                        movimentacao = f"{f'{valor:.2f} D':>30}\n"
                        num_conta = search[0]['conta']
                        
                        if extrato != []:
                            teste_extrato = False
                            for item in extrato:
                                if num_conta == item['conta']:
                                    item['movimento'] = item['movimento'] + movimentacao#concatenando 
                                    teste_extrato = True 
                            if teste_extrato != True:#caso seja False
                                extrato.append(dict({'conta':num_conta, 'movimento':movimentacao}))            
                        else:
                            extrato.append(dict({'conta':num_conta, 'movimento':movimentacao})) 
                        print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")

                    elif search[0]['saldo'] <= 0:
                        print('Saldo Insuficiente!')
            
                else:#caso possua mais de uma conta, deverá escolher
                    while True:#laço para a escolha da conta até um numero de conta valido ser digitado
                        escolha_conta = int(input('Qual conta deseja fazer saque? Digite o N° da conta: '))
                        teste_while = False #teste para caso o numero digitado não coincida com nenhuma conta do usuario
                        
                        for item in search:
                            if escolha_conta == item['conta']:
                                teste_while = True
                                valor = float(input('Digite o valor a ser sacado: '))
                                
                                lim_valor_excedido = valor > limite
                                lim_saque_excedido = item['qtd_saques_diario'] >= LIMITE_SAQUES

                                if valor <= 0:
                                    print('Valor Incorreto. Tente outro valor!')
                                elif lim_valor_excedido:
                                    print('Limite de valor diário excedido!')  
                                elif lim_saque_excedido:
                                    print('Limite de saque diário excedido!')
                                elif valor <= item['saldo']:
                                    saldo_atual = item['saldo']
                                    saldo_atual = sacar(valor_saque = valor,saldo_total=saldo_atual)#atualizando a variavel saldo_atual com o retorno da função depositar
                                    item['saldo'] = saldo_atual
                                    item['qtd_saques_diario'] += 1        

                                    movimentacao = f"{f'{valor:.2f} D':>30}\n"
                                    
                                    if extrato != []:#se o extrato não estiver vazio
                                        teste_extrato = False
                                        for item in extrato:
                                            if escolha_conta == item['conta']:
                                                item['movimento'] = item['movimento'] + movimentacao#concatenando 
                                                teste_extrato = True 
                                        if teste_extrato != True:
                                           extrato.append(dict({'conta':escolha_conta, 'movimento':movimentacao}))            
                                    else:
                                        extrato.append(dict({'conta':escolha_conta, 'movimento':movimentacao})) 
                                    
                                    print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
                                else:
                                    print('Valor incorreto. Tente outro valor!')
                        
                        if teste_while == True:
                            break #parada do laço while
                        else:
                            print(f"Conta digitada não coincide com nenhuma conta vinculada ao usuário {busca['nome']}")
            else:
                print(search)#Não há contas vinculadas ao CPF informado!
        else:
            print(busca)#O CPF () não existe na base de dados!

#MÓDULO EXTRATO
    elif opcao == 'E':
        while True:#laço para a escolha da conta até um numero de conta valido ser digitado
            escolha_conta = int(input('Digite o N° da conta que deseja visualizar o extrato: '))
            teste_while = False #teste para caso o numero digitado não coincida com nenhuma conta do usuario
                        
            for item in extrato:
                if escolha_conta == item['conta']:
                    teste_while = True
                    print(f"{'*'*31}\n{'E X T R A T O':^31}\n{'_'*31}")
                    mostrar_extrato(escolha_conta,contas,extrato)
                    print(f"{'*' *31}")  
            if teste_while == True:
                break #parada do laço while
            else:
                print(f"Conta digitada não coincide com nenhuma conta cadastrada ou a mesma não há movimentação")

#MÓDULO CADASTRO DE USUÁRIO
    elif opcao == 'C':
        while True:
            cpf_usuario = input("Digite o CPF: ").strip() 
            validador = valida_cpf(cpf_usuario)
            if validador == True:
                break
            else:
                print('Digite um CPF válido!')

        novo_usuario = criar_usuario(usuarios,cpf_usuario)
        
        if isinstance(novo_usuario,dict):#se a variavel novo_usuario for um dicionario
            usuarios.append(novo_usuario)#adiciona os dados à lista de usuarios
            print(f"Usuário {novo_usuario['nome']} cadastrado com sucesso!")
        else:
            print(novo_usuario)
    
#MÓDULO BUSCAR USUÁRIOS
    elif opcao == 'BU':
        while True:
            cpf_usuario = input("Digite o CPF: ").strip() 
            validador = valida_cpf(cpf_usuario)
            if validador == True:
                break
            else:
                print('Digite um CPF válido!')

        search = buscar_usuario(usuarios,cpf_usuario)
        if isinstance(search,dict):
            print(f"{'_'*50}\nUsuário {cpf_usuario}:\n{'-'*50}")
            print(f"Nome: {search['nome']}\nData de Nascimento: {search['data_nasc']}\nEndereço: {search['endereco']}\n{'_'*50}")
        else:
            print(search)

#MÓDULO CRIAR CONTA CORRENTE
    elif opcao == 'CC':
        while True:
            cpf_usuario = input("Iremos abrir sua conta corrente. Informe o CPF: ").strip() 
            validador = valida_cpf(cpf_usuario)
            if validador == True:
                break
            else:
                print('Digite um CPF válido!')

        nova_conta = abrir_conta(usuarios,contas,cpf_usuario)

        if isinstance(nova_conta, dict):#se a variavel nova_conta for um dicionario
            contas.append(nova_conta)#adiciona nova_conta à lista contas[]
            print(f"Conta Corrente Nº {nova_conta['conta']}, Ag: {nova_conta['agencia']} cadastrada com sucesso! ")
        else:
            print(nova_conta)

#MÓDULO BUSCAR CONTAS CORRENTE   
    elif opcao == 'BC':
        while True:
            cpf_usuario = input("Buscar contas vinculadas ao CPF: ").strip() 
            validador = valida_cpf(cpf_usuario)
            if validador == True:
                break
            else:
                print('Digite um CPF válido!')
        
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
