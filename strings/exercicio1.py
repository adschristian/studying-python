# author: Christian Alves
# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

string1 = input('Digite algum texto: ')
string2 = input('Digite algum texto: ')

tamStr1 = len(string1)
tamStr2 = len(string2)

print('Tamanho de "{}": {} caracteres'.format(string1, tamStr1))
print('Tamanho de "{}": {} caracteres'.format(string2, tamStr2))

if tamStr1 == tamStr2:
    print('As duas strings são de tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')

contentStr1 = set(string1)
contentStr2 = set(string2)

if len(contentStr1.difference(contentStr2)) == 0:
    print('As duas strings possuem conteúdo igual.')
else:
    print('As duas strings possuem conteúdo igual.')