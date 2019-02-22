# author: Christian Alves
# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
'''
a. $200 - $299
b. $300 - $399
c. $400 - $499
d. $500 - $599
e. $600 - $699
f. $700 - $799
g. $800 - $899
h. $900 - $999
i. $1000 em diante
'''

SALARIO = 200
faixa = {'$200 - $299': 0, '$300 - $399': 0, '$400 - $499': 0, '$500 - $599': 0, '$600 - $699': 0, '$700 - $799': 0, '$800 - $899': 0, '$900 - $999': 0, '$1000 ou mais': 0}
while True:
    vendas = float(input('Vendas brutas ($): '))
    if vendas < 0:
        break
    salario = SALARIO+vendas*0.09
    if salario < 300:
        faixa['$200 - $299'] += 1
    elif salario < 400:
        faixa['$300 - $399'] += 1
    elif salario < 500:
        faixa['$400 - $499'] += 1
    elif salario < 600:
        faixa['$500 - $599'] += 1
    elif salario < 700:
        faixa['$600 - $699'] += 1
    elif salario < 800:
        faixa['$700 - $799'] += 1
    elif salario < 900:
        faixa['$800 - $899'] += 1
    elif salario < 900:
        faixa['$900 - $999'] += 1
    else:
        faixa['$1000 ou mais'] += 1

for key, value in faixa.items():
    print('{}: {} vendedores'.format(key, value))