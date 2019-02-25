# author: Christian Alves
# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

soma = 0
cds = int(input('Nº de CD\'s: '))
for cd in range(cds):
    soma += float(input('Preço do CD: '))

media = soma/cds
print('Média: $ {}'.format(round(media, 2)))