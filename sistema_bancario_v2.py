menu = '''
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

'''
saldo = 0
qtd_saques = 0
limite = 500
LIMITE_SAQUES = 3
depositos = []
saques = []
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
def mostrar_extrato(valores_deposito,valores_saques,saldo_total,/):#argumentos chamados apenas por posição
    
    
    return 
#****************************************************************

while True:
    opcao = input(menu)
    
    #FUNÇÃO DEPÓSITO
    if opcao == 'd' or opcao == 'D':

        valor = float(input('Digite o valor a ser depositado: '))
        if valor > 0:
            saldo = depositar(valor,saldo)#atualizando a variavel saldo com o retorno da função depositar 
            depositos.append(valor)#adicionando valor do deposito na lista de depositos realizados
            print(f'Depósito no valor de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor incorreto. Tente outro valor!')
    
    #FUNÇÃO SAQUE
    elif opcao == 's' or opcao == 'S':
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
                saques.append(valor)
                qtd_saques += 1
                print(f'Saque no valor de R$ {valor:.2f} realizado com sucesso!')
                    
            elif saldo <= 0:
                print('Saldo Insuficiente!')

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
