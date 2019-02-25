# author: Christian Alves
# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

maior = menor = soma = cont = 0

entrada = input('Temperatura (C°): ')
if not entrada.isalpha():
    temperatura = float(entrada)
    maior = menor = soma = temperatura
    cont += 1
    
else:
    exit()

while True:
    entrada = input('Temperatura (C°): ')
    if not entrada.isalpha():
        temperatura = float(entrada)
        if temperatura > maior:
            maior = temperatura
        elif temperatura < menor:
            menor = temperatura
        soma += temperatura
        cont += 1
    else:
        break

media = soma/cont
print('Maior: {} C°'.format(maior))
print('Menor: {} C°'.format(menor))
print('Média: {} C°'.format(round(media, 2)))