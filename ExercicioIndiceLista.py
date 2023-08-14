lista = ['eric', 'henrique', 'padilha']
lista.append('alemao')
lista.append('maria')

#o range pega o tamanho da lista de forma dinamica, ou seja, se adicionarmos
#mais itens na lista, o len retornará dinamicamente os itens e seus indices
#de forma ajustada
indices = range(len(lista))

#print(indices)
#print(lista)

#para cada indice dentro da variavel indice, faca:
for indice in indices:
    #imprime o valor do I e a lista de forma separada com cada item
    print(indice, lista[indice])