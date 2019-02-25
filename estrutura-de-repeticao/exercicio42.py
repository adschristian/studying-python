# author: Christian Alves
# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

intervalo = {'0-25': 0, '26-50': 0, '51-75': 0, '76-100': 0}

while True:
    num = int(input('Digite um nº: '))
    if num > 100:
        pass
    elif num > 75:
        intervalo['76-100'] += 1
    elif num > 50:
        intervalo['51-75'] += 1
    elif num > 25:
        intervalo['26-50'] += 1
    elif num >= 0:
        intervalo['0-25'] += 1
    else:
        break

for key, value in intervalo.items():
    print('{} - {}'.format(key, value))