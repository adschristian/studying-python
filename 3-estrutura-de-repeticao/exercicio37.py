# author: Christian Alves
# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

codigo_alto = codigo_baixo = codigo_gordo = codigo_magro = alto = baixo = gordo = magro = soma_altura = soma_peso = contador = 0

code = int(input('código: '))
if code == 0:
    print('fechando o programa...')
    exit()

height = float(input('Altura (m): '))
weight = float(input('Peso (Kg): '))

codigo_alto = codigo_baixo = codigo_gordo = codigo_magro = code
alto = baixo = soma_altura = height
gordo = magro = soma_peso = weight
contador += 1

while True:
    code = int(input('código: '))
    if code == 0:
        print('imprimindo o relatório...')
        break

    height = float(input('Altura (m): '))
    weight = float(input('Peso (Kg): '))
    soma_altura += height
    soma_peso += weight

    # verificar as alturas
    if height > alto:
        codigo_alto = code
        alto = height
    elif height < baixo:
        codigo_baixo = code
        baixo = height
    
    # verificar os pesos
    if weight > gordo:
        codigo_gordo = code
        gordo = weight
    elif weight < magro:
        codigo_magro = code
        magro = weight

    contador += 1

import os

os.system('clear') or None

print('relatório')
print('maior altura\ncódigo: {}\naltura: {} m\n'.format(codigo_alto, alto))
print('menor altura\ncódigo: {}\naltura: {} m\n'.format(codigo_baixo, baixo))
print('maior peso\ncódigo: {}\npeso: {} kg\n'.format(codigo_gordo, gordo))
print('menor peso\ncódigo: {}\npeso: {} kg\n'.format(codigo_magro, magro))

media_altura, media_peso = soma_altura/contador, soma_peso/contador
print('media\naltura: {} m\npeso: {} kg'.format(round(media_altura, 2), round(media_peso, 3)))