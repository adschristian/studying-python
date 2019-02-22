# author: Christian Alves
#  Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
## a. "Telefonou para a vítima?"
## b. "Esteve no local do crime?"
## c. "Mora perto da vítima?"
## d. "Devia para a vítima?"
## e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

resultado = 0

a = input('Telefonou para a vítima? (s/n): ').lower()
if a == 's': resultado += 1
b = input('Esteve no local do crime? (s/n): ').lower()
if b == 's': resultado += 1
c = input('Mora perto da vítima? (s/n): ').lower()
if c == 's': resultado += 1
d = input('Devia para a vítima? (s/n): ').lower()
if d == 's': resultado += 1
e = input('Já trabalhou com a vítima? (s/n): ').lower()
if e == 's': resultado += 1

if resultado == 2: print('Suspeita')
elif resultado in (3, 4): print('Cúmplice')
elif resultado == 5: print('Assassino')
else: print('Inocente')
