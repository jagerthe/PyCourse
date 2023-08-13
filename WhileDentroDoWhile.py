
qtd_linhas = 5
qtd_colunas = 5

linha = 1

#enquanto essa condicao for verdadeira, ela ira executar a segunda condicao, ate 
#a segunda ser falsa
while linha <= qtd_linhas :
    coluna = 1
    while coluna <= qtd_colunas :
        print(f'{linha=} {coluna=}')
        coluna += 1
        #e so depois que essa for falsa, ele vai retornar para a primeira condicao
        #e executar tudo novamente
    linha += 1

print('Acabou')