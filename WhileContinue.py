#estruturacao de um WHILE com a palavra reservada CONTINUE

#a palavra reservada CONTINUE pode ser utilizada para pular uma linha,
#um resultado ou etc, caso nao queramos ver ele

#atentar apenas para onde ira colocar o CONTINUE, pois o mesmo pode
#ficar rodando infinitamente e estourar a memoria do computador

#instanciando a variavel que ira ser incrementada pelo WHILE
contador = 0
#definindo valor de 0 para ela nao iniciar "vazia"

while contador < 10 :
    #se nao colocar um sinal de igual, o contador ira estourar.
    contador += 1
    print(contador)

    if contador == 2 :
        print('Nao mostrarei o 2.') #obviamente ele vai mostrar um resultado aqui pois definimos isso com o print.
        continue

    if contador == 4 :
        break