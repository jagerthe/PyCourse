
lista_compras = []


print('Bem vindo ao mercado do ALEMAO!!!')

while True :
        
        print('Selecione uma opcao')
        opcoes = input('[i]nserir [a]pagar [l]istar ')

        if opcoes == 'i':
            inserir_item = input('Qual item voce deseja inserir? ')
            lista_compras.append(inserir_item)
            print(f'{inserir_item} foi adicionado a lista de compras!')


        elif opcoes == 'a':
            try: 
                deletar_item = input('Informe o indice do item que voce deseja deletar: ')
                converteValor = int(deletar_item)
                lista_compras.pop(converteValor)
                print(f'o item {deletar_item}, {inserir_item} foi removido da lista!')
            except:
                 print('O indice nao existe!')
                 continue

        elif opcoes == 'l':
                if len(lista_compras) == 0:
                     print('A lista esta vazia!')
                     
                for i, itens in enumerate(lista_compras):
                    print(i, itens)
        else:
            print('ops, algo deu errado!')
            continue