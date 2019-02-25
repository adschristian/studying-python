# author: Christian Alves
#  Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um nº: '))

if num < 2 or (num != 2 and num%2==0):
    print('não é primo')
    exit()

divisor = 3
while divisor <= num//2:
    if num%divisor == 0:
        print('não é primo')
        exit()
    divisor += 2

print('é primo')