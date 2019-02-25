# Faça um programa que peça as 4 notas bimestrais e mostre a média.
# Author: Christian Alves

nota1 = float(input('Nota 1º Bimestre: '))
nota2 = float(input('Nota 2º Bimestre: '))
nota3 = float(input('Nota 3º Bimestre: '))
nota4 = float(input('Nota 4º Bimestre: '))

media = (nota1+nota2+nota3+nota4)/4

print('Média: ' + str(media))