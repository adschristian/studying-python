# author: Christian Alves
# Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Ano: '))
if ano%400==0 or ano%4==0 and ano%100!=0:
    print('É bissexto')
else:
    print('Não é bissexto')