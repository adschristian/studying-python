# author: Christian Alves
# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono. Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do  sindicato laboral, chegou-se a seguinte forma de cálculo:
# a. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
# b. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
# O salário de cada funcionário, juntamente com o valor do abono;
# O número total de funcionário processados;
# O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais;
# O maior valor pago como abono.

import os

salarios = list()
abonos = list()
while True:
    salario = float(input('Salário (R$): '))
    if salario == 0:
        break
    salarios.append(salario)

    abono = salario*0.2

    if abono < 100:
        abono = 100.00
    
    abonos.append(abono)

    os.system('clear')

os.system('clear')

print('Projeção de Gastos com Abono\n')

for i in range(len(salarios)):
    print('R$ {:>9} - R$ {:>9}'.format(round(salarios[i], 2), round(abonos[i], 2)))
else:
    print()

colaboradores = len(salarios)
total_abonos = sum(abonos)
abono_minimo = abonos.count(100.0)
maior_abono = max(abonos)

print('Foram processados {} colaboradores'.format(colaboradores))
print('Total gasto com abonos: R$ {}'.format(round(total_abonos, 2)))
print('Valor mínimo pago a {} colaboradores'.format(abono_minimo))
print('Maior valor de abono pago: R$ {}'.format(round(maior_abono, 2)))