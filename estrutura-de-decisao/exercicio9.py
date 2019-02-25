# author: Christian Alves
# Faça um programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('Type a number: '))
num2 = int(input('Type a number: '))
num3 = int(input('Type a number: '))

if num3 > num2:
    num2, num3 = num3, num2

if num2 > num1:
    num1, num2 = num2, num1

if num3 > num2:
    num3, num2 = num2, num3

print(num1, num2, num3)