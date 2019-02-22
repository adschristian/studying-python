# author: Christian Alves
# Faça um programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

a = list()
tam = 10

for i in range(tam):
    num = int(input('Digite um nº: '))
    a.append(num)

quadrados = list(map(lambda x: x**2, a))
print('Soma dos quadrados: {}'.format(sum(quadrados)))