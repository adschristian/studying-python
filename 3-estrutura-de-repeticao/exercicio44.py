# author: Christian Alves
# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
'''
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''

from os import system

candidatos = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'nulo': 0, 'branco': 0}

while True:
    print('Candidatos')
    print('1) Zé\n2) Rui\n3) Cauê\n4) Ana\n5) Voto em Branco')
    voto = input('Voto: ')
    
    if voto == '1':
        candidatos['a'] += 1
    elif voto == '2':
        candidatos['b'] += 1
    elif voto == '3':
        candidatos['c'] += 1
    elif voto == '4':
        candidatos['d'] += 1
    elif voto == '5':
        candidatos['branco'] += 1
    elif voto == '0':
        system('clear')
        break
    else:
        candidatos['nulo'] += 1
    
    system('clear')


total = sum(candidatos.values())
print('Total de votos: {}\n'.format(total))

print('Votos por candidato')
for candidato, votos in candidatos.items():
    print('{} - {} votos'.format(candidato, votos))

porcentagemNulos = total*candidatos['nulo']
print('% votos nulos: {}%'.format(porcentagemNulos))

porcentagemBrancos = total*candidatos['branco']
print('% votos em branco: {}%'.format(porcentagemBrancos))