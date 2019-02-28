# author: Christian Alves
# Faça um programa que leia 5 números e informe o maior número.

num = int(input('Digite um número: '))
maior = num
for i in range(4):
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num

print('Maior: {}'.format(maior))