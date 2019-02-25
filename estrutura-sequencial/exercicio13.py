# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7 (h = altura)
# c. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
# Author: Christian Alves

altura = float(input('Altura (m): '))
sexo = input('Sexo (m/f): ').lower()

print('Peso ideal')
print('Homem: {}'.format((72.7*altura)-58))
print('Mulher: {}'.format((62.1*altura)-44.7))