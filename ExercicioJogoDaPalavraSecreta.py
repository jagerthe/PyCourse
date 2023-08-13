palavra = 'cabide'
letras_acertadas = ['*'] * len(palavra)
tentativas = 6

print('Bem vindo ao jogo da palavra secreta!')
print('A Palavra possui', len(palavra), 'letras, e voce possui:', tentativas, 'tentativas!')
print(' '.join(letras_acertadas))

while '*' in letras_acertadas and tentativas > 0:
    letra = input('Digite uma letra: ')
    if letra.isalpha() == False:
        print('Voce informou um numero ou caractere invalido, por favor, digite uma letra: ')
        continue
    else:
        print('')
        
    try:
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_acertadas[i] = letra
                    print(letras_acertadas)

        if len(letra) > 1:
            print('Voce informou mais de uma letra por vez, por favor, informe apenas uma! ')
            continue
        elif letra not in palavra:
            tentativas -= 1
            print(f'Letra incorreta! Voce tem {tentativas} tentativas restantes!')
            continue
            
        

    except:
        print('Algo deu errado....')

if '*' not in letras_acertadas:
    print(f'Parabens, voce acertou! A palavra era = {palavra}!')
else:
    print('Voce nao conseguiu...')