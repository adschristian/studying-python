# author: Christian Alves
# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    num = int(input('Fatorial de: '))
    while num >= 16:
        num = int(input('Fatorial de: '))

    fat = 1
    for i in range(num, 1, -1):
        fat *= i

    print('{}! = {}'.format(num, fat))

    if input('Calcular outro fatorial? (s/n) ') != 's':
        exit()