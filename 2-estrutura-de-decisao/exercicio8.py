# author: Christian Alves
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco = float(input('Preço $: '))
menor = preco
preco = float(input('Preço $: '))
if preco < menor: menor = preco
preco = float(input('Preço $: '))
if preco < menor: menor = preco

print('Menor preço: $ {}'.format(round(menor, 2)))