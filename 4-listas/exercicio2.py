# author: Christian Alves
# Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = list()

for i in range(10):
    numero = float(input('Digite um nº: '))
    lista.append(numero)

print(lista[::-1])