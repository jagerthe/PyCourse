"""CALCULADORA COM WHILE"""

while True :
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite um operador(+-/*): ')

    numeros_validos = None

    numero1 = 0
    numero2 = 0

    try :
        numero1 = float(numero_1)
        numero2 = float(numero_2)
        numeros_validos = True

    
    except :
        numeros_validos = None

        if numeros_validos is None:
            print('Um ou mais numeros digitados sao invalidos!')
            continue

        operadores_permitidos = '+-/*'

        if operador not in operadores_permitidos:
            print('O operador nao é permitido!')
            continue

        if len(operador) > 1:
            print('Apenas um operador por vez.')
            continue

    #########

    print('Executando a conta: ')
    if operador == '+' :
        print(numero1 + numero2)
    elif operador == '-' :
        print(numero1 - numero2)
    elif operador == '/' :
        print(numero1 / numero2)
    elif operador == '*' :
        print(numero1 * numero2)
    else :
        print('Voce nao deveria ter chegado aqui...')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True :
        print('Voce escolheu sair.')
        break
