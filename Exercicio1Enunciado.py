

numero = input('Informe um numero, e eu direi se é PAR ou IMPAR: ')


try :
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar :
        par_impar_texto = 'par'

    print(f'o numero {numero_int} é {par_impar_texto}')
except :
    print('Isso era pra ser um numero inteiro?')