# author: Christian Alves
# Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
## a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
## b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor = int(input('Valor a sacar: '))
if valor > 600 or valor < 10:
    print('Não é possível sacar.')
    exit()

aux = valor

if aux >= 100:
    quant = aux//100
    aux -= quant*100
    print('R$ 100,00: {}'.format(quant))
if aux >= 50:
    quant = aux//50
    aux -= quant*50
    print('R$ 50,00: {}'.format(quant))
if aux >= 10:
    quant = aux//10
    aux -= quant*10
    print('R$ 10,00: {}'.format(quant))
if aux >= 5:
    quant = aux//5
    aux -= quant*5
    print('R$ 5,00: {}'.format(quant))
if aux >= 1:
    print('R$ 1,00: {}'.format(aux))