# author: Christian Alves
# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

semana = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']

dia = int(input('Digite um nº: '))-1
print('Valor inválido.' if dia > 6 or dia < 0 else semana[dia])