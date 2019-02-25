# Author: Christian Alves
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import ceil

area = int(input('Área (m³): '))
litros = ceil(area/6)
latas = ceil(litros/18)
galoes = ceil(litros/3.6)

print('Latas: {}\nPreço total: R$ {}'.format(latas, round(latas*80, 2)))
print('Galões: {}\nPreço total: R$ {}'.format(galoes, round(galoes*25, 2)))

total_l = 0
galao = 0
lata = 0

while litros-total_l > 0:
    if litros-total_l > 18:
        lata += 1
    else:
        galao += 1
    
    if galao > 3:
        lata += 1
        galao = 0
    
    total_l = galao*3.6+lata*18

preco_total = galao*25+lata*80
print('\n')
print('Latas: {}\nGalões: {}\nPreço total: R$ {}'.format(lata, galao, round(preco_total, 2)))
