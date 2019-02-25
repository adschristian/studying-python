# author: Christian Alves
# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for i in range(5):
    soma += int(input('Digite um nº: '))

media = soma/5
print('Soma: {}\nMédia: {}'.format(soma, round(media, 1)))