# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7 * altura) - 58
# Author: Christian Alves

altura = float(input('Type your height: '))
peso_ideal = 72.7*altura-58
print('Ideal weight: {}'.format(peso_ideal))