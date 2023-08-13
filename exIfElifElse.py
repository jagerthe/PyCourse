print('Informe dois valores e descubra qual é maior que qual: ')
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

if primeiro_valor > segundo_valor :
    print(f'primeiro_valor={primeiro_valor} maior que segundo_valor={segundo_valor}')
elif primeiro_valor < segundo_valor :
    print(f'segundo_valor="{segundo_valor} maior que primeiro_valor={primeiro_valor}')
else :
    print('fim do programa!')
    