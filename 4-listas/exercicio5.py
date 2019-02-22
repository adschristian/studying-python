# author: Christian Alves
# Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = list()

for i in range(20):
    num = int(input('Digite um nº: '))
    numeros.append(num)

pares = []
impares = []
for num in numeros:
    if num%2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('Números: {}\nPares: {}\nÍmpares: {}'.format(numeros, pares, impares))