

horario = input('Informe que horas sao agora: ')
minutos = input('Informe os minutos')

try :
    if int(horario) >= 0 and int(horario) <=11 :
       print('Bom dia!')
    elif int(horario) >= 12 and int(horario) <= 17 :
        print('Boa tarde!')
    else :
        print('Boa noite!')
except :
    print('nao conheco essa hora!')