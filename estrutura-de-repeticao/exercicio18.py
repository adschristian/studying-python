# author: Christian Alves
# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = int(input('Nº de iterações: '))

num = int(input('Digite um nº: '))
maior = menor = soma = num
for i in range(1, n):
    num = int(input('Digite um nº: '))
    soma += num
    if num > maior: maior = num
    elif num < menor: menor = num

print('Maior: {:>2}'.format(maior))
print('Menor: {:>2}'.format(menor))
print('Soma:  {:>2}'.format(soma))
