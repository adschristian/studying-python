# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# Author: Christian Alves

valor = float(input('Salário/Hora: '))
horas = int(input('Horas/Mês: '))
salario = valor * horas

print('Salário/Mês: $ ' + str(salario))