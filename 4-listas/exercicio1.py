# author: Christian Alves
# Faça um programa que leia um vetor de 5 números inteiros e mostre-os.

lista = list()

for i in range(5):
    numero = int(input('Digite um nº: '))
    lista.append(numero)

print(lista)