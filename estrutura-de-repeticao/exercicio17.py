# author: Christian Alves
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n = int(input('Fatorial de: '))

fat = 1
for i in range(n, 1, -1):
    fat *= i

print('{}! = {}'.format(n, fat))