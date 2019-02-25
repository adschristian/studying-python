# author: Christian Alves
# Faça um programa que leia 4 notas, mostre as notas e a média na tela.

notas = list()

for i in range(4):
    nota = float(input('{}ª nota: '.format(i+1)))
    notas.append(nota)

print('Notas: {}'.format(notas))
media = sum(notas)/len(notas)
print('Média: {}'.format(round(media, 1)))