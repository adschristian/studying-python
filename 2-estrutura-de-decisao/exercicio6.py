# author: Christian Alves
# Faça um programa que leia três números e mostre o maior deles.

num = int(input('Type a number: '))
maior = num
num = int(input('Type a number: '))
if (num > maior): maior = num
num = int(input('Type a number: '))
if (num > maior): maior = num

print('Maior: ' + str(maior))