# author: Christian Alves
# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# # o salário antes do reajuste;
# # o percentual de aumento aplicado;
# # o valor do aumento;
# # o novo salário, após o aumento.

salario_bruto = float(input('Salário (R$): '))
aumento = 0
print('R$ {}'.format(round(salario_bruto, 2)))
if salario_bruto > 1500:
    print('Reajuste de 5%')
    aumento = salario_bruto*0.05
elif salario_bruto > 700:
    print('Reajuste de 10%')
    aumento = salario_bruto*0.1
elif salario_bruto > 280:
    print('Reajuste de 15%')
    aumento = salario_bruto*0.15
else:
    print('Reajuste de 20%')
    aumento = salario_bruto*0.2

print('Aumento: R$ {}'.format(round(aumento, 2)))
print('Salário reajustado: R$ {}'.format(round(salario_bruto+aumento, 2)))