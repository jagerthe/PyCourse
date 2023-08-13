nome = 'eric biao'
altura = 1.82
peso = 90
imc = peso / (altura * altura)

#texto sem formatacao
print('O paciente', nome, 'pesa', peso, 'quilos e seu imc é', imc)

#texto formatado
linha_1 = f'{nome} tem {altura:.2f} de altura'
print(linha_1)

#f é a sigla para a linha entender que vira formatacao
#{} é para receber e ler as variaveis
#.2f é para definir quantas casas vao aparecer depois do .