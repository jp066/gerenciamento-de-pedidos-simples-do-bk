from arquivo import cadastrar

arq = 'pedidos.txt'

pedidos = []


def mostrarLinhas():
    print('-' * 50)
    

def opcao():
    print('Entre as opção listadas: ')
    print('1 - Cadastrar pedido')
    print('2 - Consultar pedido')
    print('3 - Sair')
    print('4 - area de pagamento')
    opcaoEscolhida = int(input('Digite a opção desejada: '))
    mostrarLinhas()
    
    while True:
        if opcaoEscolhida == 1:
            print('Opção escolhida: Cadastrar pedido')
            print('1 - BK chips e Coca-Cola: R$ 20,00')
            print('2 - BK fritas e Pepsi: R$ 18,00')
            print('3 - BK onion rings e Fanta: R$ 22,00')
            print('4 - BK chicken fries e Guaraná: R$ 25,00')
            comboDesejado = int(input('Digite o número do combo desejado: '))
            pedidos.append(comboDesejado)
            cadastrar(arq, comboDesejado)
            mostrarLinhas()
            continuar = input('Deseja continuar? [S/N] ').upper()
            mostrarLinhas()
            if continuar in 'SimsimSIM':
                opcao()
            else:
                print('Obrigado por usar o sistema de gerenciamento de pedidos do Burguer King da Raul Lopes.')
                break
    
        elif opcaoEscolhida == 2:
            print('Opção escolhida: Consultar pedido')
            numPedido = int(input('Digite o número do pedido ou veja todos os pedidos(0): '))
            if numPedido == 0:
                print(f'Pedidos: {pedidos}')
            else:
                print(f'Pedido {numPedido}: Em andamento')
            mostrarLinhas()
            continuar = input('Deseja continuar? [S/N] ').upper()
            mostrarLinhas()
            if continuar in 'SimsimSIM':
                opcao()
            else:
                print('Obrigado por usar o sistema de gerenciamento de pedidos do Burguer King da Raul Lopes.')
                break
            
            
        elif opcaoEscolhida == 3:
            print('Opção escolhida: Sair')
            print('Obrigado por usar o sistema de gerenciamento de pedidos do Burguer King da Raul Lopes.')
        break