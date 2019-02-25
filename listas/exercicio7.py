# author: Christian Alves
# Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = list()
for i in range(5):
    num = int(input('Digite um nº: '))
    numeros.append(num)

print('Soma: {}'.format(sum(numeros)))

import functools

mult = functools.reduce(lambda x, y: x * y, numeros)

print('Multiplicação: {}'.format(mult))