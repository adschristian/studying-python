# author: Christian Alves
# Faça um programa que leia três números e mostre o maior e o menor deles.

num = int(input('Type a number: '))
maior = num
menor = num
num = int(input('Type a number: '))
if num > maior: maior = num
elif num < menor: menor = num
num = int(input('Type a number: '))
if num > maior: maior = num
elif num < menor: menor = num

print('Maior: {0}\nMenor: {1}'.format(maior, menor))