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
extrato = ''

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
def mostrar_extrato(movimentacao,/,*,saldo_total):#argumentos chamados apenas por posição
    if extrato == '':
        #saida = (f"\n{f'Sem movimentação':>31}" if extrato == '' else movimentacao)
        saida = f"{f'Sem movimentação':>31}\n{'_'*31}\n{f'Saldo: R$ {saldo_total:.2f}  ':>31}\n"
    else:
        saida = f"{movimentacao}\n{'_'*31}\n{f'Saldo: R$ {saldo_total:.2f}  ':>31}\n"
    
    return saida
#****************************************************************

while True:
    opcao = input(menu)
    
    #MÓDULO DEPÓSITO
    if opcao == 'd' or opcao == 'D':

        valor = float(input('Digite o valor a ser depositado: '))
        if valor > 0:
            saldo = depositar(valor,saldo)#atualizando a variavel saldo com o retorno da função depositar 
            extrato = f"{extrato}\n {f'R$ {valor:.2f} C':>30}"
            print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")
            
        else:
            print('Valor incorreto. Tente outro valor!')
    
    #MÓDULO SAQUE
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
                qtd_saques += 1
                extrato = f"{extrato}\n {f'R$ {valor:.2f} D':>30}"
                print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
                    
            elif saldo <= 0:
                print('Saldo Insuficiente!')

    #MÓDULO EXTRATO
    elif opcao == 'e' or opcao == 'E':
        
        print(f"{'*'*31}\n{'E X T R A T O':^31}\n{'_'*31}")
        print(mostrar_extrato(extrato,saldo_total=saldo))#chamando função mostrarextrato() com argumentos posicionais e nominais
        print(f"{'*' *31}")  

    #SAIR
    elif opcao == 'q' or opcao == 'Q':
        break
    
    else:
        print('Opção inválida. Escolha outra opção!')
