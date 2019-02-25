# author: Christian Alves
# Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

tam = 10
vetor1 = []
vetor2 = []
print('vetor 1')
for i in range(tam):
    num = int(input('Digite um nº: '))
    vetor1.append(num)

print('vetor 2')
for i in range(tam):
    num = int(input('Digite um nº: '))
    vetor2.append(num)

composto = []
for i in range(tam):
    composto.append(vetor1[i])
    composto.append(vetor2[i])

print('Composto: {}'.format(composto))