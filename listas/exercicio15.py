# author: Christian Alves
# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
'''
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;
'''

numeros = list()

while True:
    num = float(input('Digite um nº: '))
    if num == -1:
        break

    numeros.append(num)

import os

os.system('clear')

print('Nº de valores lidos: {}'.format(len(numeros)))
print(*numeros, sep=' ')
print(*numeros[::-1], sep='\n')
total = sum(numeros)
print('Soma dos valores: {}'.format(total))
media = total/len(numeros)
print('Média: {}'.format(media))
print('Média dos valores: {}'.format(media))
acima = len(list(filter(lambda x: x > media, numeros)))
print('Acima da média: {} valores'.format(acima))
acimaSete = len(list(filter(lambda x: x < 7.0, numeros)))
print('Abaixo de 7.0: {} valores'.format(acimaSete))
print('Top')