# Author: Christian Alves
# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido
# Salário bruto - IR (11%) - INSS (8%) - Sindicato (5%) = Salário líquido

salario_hora = float(input('Salário/Hora: '))
horas_mes = int(input('Horas/Mês: '))

salario_bruto = salario_hora*horas_mes

ir = salario_bruto*0.11
inss = salario_bruto*0.08
sind = salario_bruto*0.05
salario_liquido = salario_bruto-ir-inss-sind

print('Salário bruto: $ {}'.format(round(salario_bruto, 2)))
print('Imposto de renda: $ {}'.format(round(ir, 2)))
print('INSS: $ {}'.format(round(inss, 2)))
print('Sindicato: $ {}'.format(round(sind, 2)))
print('Salário líquido: $ {}'.format(round(salario_liquido, 2)))