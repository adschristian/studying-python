# author: Christian Alves
# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
'''
Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''

import os

while True:
    nome = input('Para sair pressione [Enter]\nNome do atleta: ')
    if nome.strip() == '':
        exit()

    saltos = list()
    for i in range(5):
        salto = float(input('{}º salto (m): '.format(i+1)))
        saltos.append(salto)

    os.system('clear')
    
    print('Resultado final')
    print('Atleta: {}'.format(nome))
    print('Saltos: ', end='')
    print(*saltos, sep=' - ')
    media = sum(saltos)/len(saltos)
    print('Média dos saltos: {} m'.format(media))
    input('\nPressione [Enter] para continuar...')
    os.system('clear')