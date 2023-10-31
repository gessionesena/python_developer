menu = '''
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

'''
saldo = 0
limite = 500
qtd_saques = 0
LIMITE_SAQUES = 3
depositos = []
saques = []

while True:
    opcao = input(menu)
    
    #FUNÇÃO DEPÓSITO
    if opcao == 'd' or opcao == 'D':

        deposito = float(input('Digite o valor a ser depositado: '))
        if deposito > 0:
            depositos.append(deposito)#guarda valor na lista de depositos
            saldo += deposito #atualizando saldo
        else:
            print('Valor incorreto. Tente outro valor!') 
    
    #FUNÇÃO SAQUE
    elif opcao == 's' or opcao == 'S':

        saque = float(input('Digite o valor a ser sacado:'))
        if saque > 0:
            if saque <= saldo:
                if qtd_saques < LIMITE_SAQUES:
                    if saque <= limite:
                        qtd_saques += 1 #atualizando qtd_saques
                        saldo -= saque #atualizando saldo
                        saques.append(saque) #guarda valor na lista de saques
                        print('Saque realizado com sucesso!')
                    else:
                        print('Valor excede o limite diário. Tente outro valor!')
                else:
                    print('Limite de saque diário excedido. Tente novamente em outro dia!')       
            else:
                print('Saldo insuficiente. Tente outro valor!')
        else:
            print('Valor incorreto. Digite novamente!')
            
    #FUNÇÃO EXTRATO
    elif opcao == 'e' or opcao == 'E':
        
        def listar_valores(lista):
            for valores in lista:
                print(f'R$ {valores:.2f}')
        
        print('*********************\n--- E X T R A T O ---\n*********************\nCréditos\n')
        
        print('Nenhuma movimentação!') if not depositos else listar_valores(depositos)#condição para verificar se a lista está vazia

        print('\nDébitos\n')

        print('Nenhuma movimentação!') if not saques else listar_valores(saques)#condição para verificar se a lista está vazia

        print(f'\n---------------------\nSaldo: {saldo:.2f}\n*********************\n')     

    #FUNÇÃO SAIR
    elif opcao == 'q' or opcao == 'Q':
        break
    
    else:
        print('Opção inválida. Escolha outra opção!')
