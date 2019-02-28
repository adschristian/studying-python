# author: Christian Alves
# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
# a. O modelo do carro mais econômico;
# b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.

import os

carros = dict()
KM = 100
PRECO = 2.25

for i in range(5):
    print('Comparativo de Consumo\n')
    carro = input('Modelo do carro: ')
    km_litro = float(input('Km/Litro: '))
    carros[carro] = km_litro
    os.system('clear')

print('Relatório final\n')

consumo_menor = None
carro_menor = None

for carro, km in carros.items():
    consumo = KM/km

    if consumo_menor is None:
        consumo_menor = consumo
        carro_menor = carro
    elif consumo < consumo_menor:
        consumo_menor = consumo
        carro_menor = carro

    custo = PRECO*consumo
    print('{:15} - {:>5} - {:>5} - R$ {:>5}'.format(carro, km, round(consumo, 1), round(custo, 2)))

print('O menor consumo é do {}.'.format(carro_menor))