# author: Christian Alves
# Faça um programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input('Digite um nº: '))
print('Inteiro' if numero==round(numero) else 'Decimal')