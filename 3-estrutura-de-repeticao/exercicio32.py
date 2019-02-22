# author: Christian Alves
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! = 5 . 4 . 3 . 2 . 1 = 120


n = int(input('Fatorial de: '))

fat = 1
print('Fatorial de: {}'.format(n))
print('{}! ='.format(n), end=' ')
for i in range(n, 1, -1):
    print('{}'.format(i), end=' ')
    if i == 2:
        print('. 1 = ', end='')
    else:
        print('. ', end='')
    fat *= i

print('{}'.format(fat))