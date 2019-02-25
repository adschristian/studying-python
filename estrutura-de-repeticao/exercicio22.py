# author: Christian Alves
# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input('Digite um nº: '))

divisores = list()
primo = True
if num < 2:
    exit()

if num != 2 and num%2==0:
    primo = False
    divisores.append(2)

divisor = 3

while divisor <= num//2:
    if num%divisor == 0:
        if primo:
            primo = False
        divisores.append(divisor)
    divisor += 2

if primo:
    print('é primo')
else:
    print('não é primo')
    print('divisores: {}'.format(divisores))