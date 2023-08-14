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

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
#concatenando duas listas em uma só
lista_c = lista_a + lista_b
#nessa concatencao, ele une as duas listas, gerando uma nova
print(lista_c)

#fazendo uma extensao de lista
lista_a.extend(lista_b)
#nessa extensao, ele pega os elementos da lista_b e incrementa na lista_a
#ou seja, ele teoricamente nao alterou nada da lista_b, apenas uniu ela a 
#lista_a, a unica lista alterada de fato foi a lista_a
print(lista_a)