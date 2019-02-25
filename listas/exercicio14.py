# author: Christian Alves
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
'''
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3
e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

respostas = list()
res = input('Telefonou para a vítima? (s/n) ')
respostas.append(True if res.lower() == 's' else False)

res = input('Esteve no local do crime? (s/n) ')
respostas.append(True if res.lower() == 's' else False)

res = input('Mora perto da vítima? (s/n) ')
respostas.append(True if res.lower() == 's' else False)

res = input('Devia para a vítima? (s/n) ')
respostas.append(True if res.lower() == 's' else False)

res = input('Já trabalhou com a vítima? (s/n) ')
respostas.append(True if res.lower() == 's' else False)

total = sum(respostas)

if total == 5:
    print('Assassino')
elif total in (3,4):
    print('Cúmplice')
elif total == 2:
    print('Suspeita')
else:
    print('Inocente')