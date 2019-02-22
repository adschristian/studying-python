# author: Christian Alves
# Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input('Nº de notas: '))

soma = 0
for i in range(n):
    soma += float(input('Nota {}: '.format(i+1)))

media = soma/n
print('Média: {}'.format(media))