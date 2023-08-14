"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]

#alteramos o indice 2 da lista para 300
    #lista[2] = 300
#deletamos o indice 2 da lista
    #del lista[2]

#adicionamos um valor ao final da lista
lista.append(50)
#deletamos o ultimo valor da lista
#lista.pop()
lista.append(60)
lista.append(70)
lista.append(80)
#tambem podemos usar o pop com o indice do item na lista
#para direcionar qual item queremos deletar
ultimo_valor = lista.pop(2)

print(lista, 'removido,', ultimo_valor)