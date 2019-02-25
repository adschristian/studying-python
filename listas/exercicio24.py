# author: Christian Alves
# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

from random import randint

dados = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(100):
    n = randint(1, 6)
    print('valor = {}'.format(n))
    dados[n] += 1
else:
    print()

for num, qtd in dados.items():
    print('{}: {} vezes'.format(num, qtd))
