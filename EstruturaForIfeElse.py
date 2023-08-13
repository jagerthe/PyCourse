#declarando a palavra chave FOR e atribuindo seus metodos
#logo apos do for, declaramos uma variavel com o nome de indice
#e seu range de 10, ou seja, 10 repeticoes
for i in range(10) :
    #se o indice for igual a 2, executara essa linha e ira pular a rodada, indo
    #direto do 1 para o 3
    if i == 2:
        print('I recebeu 2, portanto pulando...')
        #continue é a palavra chave reservada para pular uma rodada do for
        continue
    
    #se o indice for igual a 8, entao ele encerrara o programa, e nao executará o else,
    #pois o mesmo se encontra dentro do FOR
    if i == 8 :
        print('seu I recebeu 8, portanto seu else nao executará...')
        #break é a palavra reservada utilizada para forcar o encerramento da aplicacao
        #interessante de usar para quando o usuario ja esta satisfeito com o programa
        #e deseja encerrar o mesmo, forcando uma saida
        break

    #feito mais um laco de repeticao dentro do FOR principal, esse ira pegar o valor do
    #indice e irá printar ao lado dele, um valor, estilo coluna, ou seja, ira imprimirir
    #para cada rodada do indice, os valores passados para a coluna, no exemplo aqui
    #pegará dois valores do indice e o repetirá ate satisfazer a condicao
    for j in range(1, 3) :
        print(i, j)
#else sera executado somente quando o metodo acabar, como definimos um ponto de break
#no meio do laco, setando o valor 8 como forma de encerramento, nunca cairemos nesse else
#apenas se comentarmos ou removermos o if == 8
else :
    print('Laco FOR completo com sucesso')