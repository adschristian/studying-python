# author: Christian Alves
# Faça um programa que peça dois números e imprima o maior deles.

a = int(input('Type a number: '))
b = int(input('Type another number: '))

print('Maior = ', end='')
if a > b: print(a)
elif b > a: print(b)
else: print('nenhum')