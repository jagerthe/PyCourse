"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#         0,  1,  2,  3
lista = [10, 20, 30, 40]
#lista.append('eric')
#lista.pop()
#lista.append(1234)
#del lista[-1]
#lista.clear()

#podemos inserir um valor onde a gente quiser na lista com o INSERT
#o proprio python vai ajustar a lista, porem se a lista for muito grande
#pode causar lentidao na aplicacao
#            i,  item
lista.insert(4, 100)
print(lista)