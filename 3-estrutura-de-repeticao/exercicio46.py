# author: Christian Alves
# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução,  portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
'''
Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Melhor salto: 6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m
Resultado final:
Rodrigo Curvêllo: 5.9 m
'''

from os import system

while True:
    nome = input('Atleta: ')
    if nome == '':
        break

    saltos = list()
    for i in range(5):
        distancia = float(input('{}º Salto (m): '.format(i+1)))
        saltos.append(distancia)
    
    system('clear')

    print('Atleta: {}'.format(nome))
    for i in range(5):
        print('{}º salto: {} m'.format(i+1, saltos[i]))
    
    saltos.sort(reverse=True)

    print()
    print('Melhor salto: {} m'.format(saltos[0]))
    print('Melhor salto: {} m'.format(saltos[-1]))
    mediaSaltos = sum(saltos[1:4])/3
    print('Média dos demais saltos: {} m'.format(round(mediaSaltos)))

    print('\nResultado final\n{}: {} m'.format(nome, round(mediaSaltos)))