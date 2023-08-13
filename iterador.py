'''

Iteravel -> str, range, etc, (__iter__) #iteraveis sao funcoes
Iterador -> quem sabe entregar um valor por vez
Next -> me entregue o proximo valor
Iter -> me entregue seu iterador
'''

#texto = iter('eric') #__iter__()
'''
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
#quando acabar os valores, ele levantara um erro
#ideal que seja tratado com TRY EXCEPTION
'''

#outra forma de fazer um next
#print(next(texto))

texto = 'eric' #iteravel
iterador = iter(texto) #iterador

#executando praticamente a mesma coisa que em um FOR
#for letra in texto
while True: 
    #executando um try para tentar fazer alguma coisa
    #enquanto nao estourar erro
    try:
        letra = next(iterador)
        print(letra)
    #passando um parametro de erro para o except, para o mesmo
    #capturar e tratar, assim impedindo que a aplicacao estoure
    #a memoria
    except StopIteration:
        break