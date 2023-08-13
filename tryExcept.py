numero_str = input('vou dobrar o numero que voce digitar: ')

try :
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_str)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except :
    print('isso nao é um numero o vagabundo')