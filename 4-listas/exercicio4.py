# author: Christian Alves
# Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

chars = list()

for i in range(10):
    char = input('Digite uma letra: ')
    chars.append(char)

consoantes = list()
for char in chars:
    if char.lower() not in ('a','e','i','o','u') and len(char) == 1 and char.isalpha():
        consoantes.append(char)

print('Consoantes: {}'.format(len(consoantes)))
print('{}'.format(consoantes))