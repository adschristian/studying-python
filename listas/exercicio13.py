# author: Christian Alves
# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperaturas = dict()
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
for i in range(12):
    temp = float(input('Temperatura média de {} (C°): '.format(meses[i].capitalize())))
    temperaturas[meses[i]] = temp

media_anual = sum(temperaturas.values())/len(temperaturas)

for mes, temp in temperaturas.items():
    if temp > media_anual:
        print('{}: {} C°'.format(mes, temp))