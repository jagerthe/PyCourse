'''
FOR + RANGE
range -> range(start, stop, step)

'''
#definimos apenas o start, que pega de 0 a 10
#numeros = range(10)
#print(numeros)

#definimos o start, no zero, definimos para parar no 10 e definimos
#que pule de 1 em 1
numeros = range(0, 100, 2)
#print(numeros)

#agora encaixamos range com for para fazer a impressao na tela completa
#da lista dos numeros

for numero in numeros :
    print(numero)