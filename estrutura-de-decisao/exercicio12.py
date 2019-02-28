# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
## Salário Bruto até 900 (inclusive) - isento
## Salário Bruto até 1500 (inclusive) - desconto de 5%
## Salário Bruto até 2500 (inclusive) - desconto de 10%
## Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações

salario_hora = float(input('Salário/Hora: '))
horas_mes = int(input('Horas/Mês: '))
salario_bruto = salario_hora * horas_mes

print('Salário Bruto: ({} * {}): R$ {}'.format(salario_hora, horas_mes, round(salario_bruto, 2)))

desconto_ir = 0
desconto_inss = 0
desconto_sind = 0

if salario_bruto > 2500:
    ir = 20
    desconto_ir = salario_bruto*0.2
elif salario_bruto > 1500:
    ir = 10
    desconto_ir = salario_bruto*0.1
elif salario_bruto > 900:
    ir = 5
    desconto_ir = salario_bruto*0.05
else:
    ir = 'Isento'

desconto_inss = salario_bruto*0.1
desconto_sind = salario_bruto*0.03
fgts = salario_bruto*0.11
total_descontos = salario_bruto-desconto_ir-desconto_inss-desconto_sind

print('(-) IR ({}%): R$ {}'.format(ir, round(desconto_ir, 2)))
print('(-) INSS (10%): R$ {}'.format(round(desconto_inss, 2)))
print('(-) Sindicato (3%): R$ {}'.format(round(desconto_sind, 2)))
print('FGTS (11%): R$ {}'.format(round(fgts, 2)))
print('Total de descontos: R$ {}'.format(round(total_descontos, 2)))