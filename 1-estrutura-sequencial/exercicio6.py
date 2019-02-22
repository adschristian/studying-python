# Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
# Author: Christian Alves

from math import pi
raio = float(input('Raio: '))
area = (raio**2)*pi
print('Area: ' + str(area) + ' um')