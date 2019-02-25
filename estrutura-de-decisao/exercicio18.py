# author: Christian Alves
# Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input('Data (dd/mm/aaaa): ')

if len(data) > 10:
    print('Data inválida')
    exit()

aux = data.split('/')

if len(aux) != 3:
    print('Data inválida')
    exit()

dia = int(aux[0])
mes = int(aux[1])
ano = int(aux[2])

mes31 = [1,3,5,7,8,10,12]
mes30 = [4,6,9,11]

if mes in mes31:
    if dia>31:
        print('Data inválida')
        exit()
elif mes in mes30:
    if dia>30:
        print('Data inválida')
        exit()
else:
    if ano%400==0 or ano%4==0 and ano%100!=0:
        if dia>29:
            print('Data inválida')
            exit()
    else:
        if dia>28:
            print('Data inválida')
            exit()

print('Data válida')