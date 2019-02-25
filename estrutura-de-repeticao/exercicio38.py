# author: Christian Alves
# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
'''
a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

from datetime import datetime

salario = float(input('Salário inicial (R$): '))
limite = datetime.now().year
percentual = 0.015
for ano in range(1996, limite+1):
    salario += salario * percentual
    print(salario)
    percentual *= 2

print('Salário: R$ {}'.format(round(salario, 2)))