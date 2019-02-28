# author: Christian Alves
# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

cod_alto = cod_baixo = alto = baixo = 0
code = int(input('Código: '))
height = int(input('Altura (cm): '))

cod_alto = cod_baixo = code
alto = baixo = height

for i in range(9):
    code = int(input('Código: '))
    height = int(input('Altura (m): '))

    if height > alto:
        cod_alto = code
        alto = height
    elif height < baixo:
        cod_baixo = code
        baixo = height

print('mais alto\ncódigo: {}\naltura: {} cm\n'.format(cod_alto, alto))
print('mais baixo\ncódigo: {}\naltura: {} cm'.format(cod_baixo, baixo))