"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

"""
#posicao de cada item na lista
#         0     1        2        3    4
#        -1    -2       -3       -4   -5
lista = [123, True, 'eric biao', 1.2, []]

print(lista)
print(lista[2], type(lista[2]))

#alterando um item na lista por sua posicao
lista[-3] = 'maria'
print(lista)