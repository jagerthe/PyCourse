#Exemplo de While com Else

string = 'eric biao'

#i = indice
i = 0
#enquanto o indice for menor que o tamanho da string,
while i < len(string) :
    #adicionar uma letra do indice da string na variavel letra
    letra = string[i]

    #se a palavra tiver espaco, vai travar no espaco e vai terminar
    if letra == ' ' :
        break

    #do contrario, vai imprimir na tela o indice + cada letra da palavra, uma por vez
    print(letra)
    i += 1

else :
    print('Dentro do while')

print('fora do while')