
nome = input('Digite seu nome: ')

tamanho_nome = len(nome)
print(tamanho_nome)

if tamanho_nome > 2 :
    if tamanho_nome <= 4 :
       print('Seu nome é muito pequeno!')
    elif tamanho_nome >= 5 and tamanho_nome <= 6 :
        print('Seu nome é normal!')
    else :
        print('seu nome é mt grande!')
else :
    print('digite pelo menos duas letras...') 
  