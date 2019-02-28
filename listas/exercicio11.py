# author: Christian Alves
# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

tam = 10
vetor1 = []
vetor2 = []
vetor3 = []
print('vetor 1')
for i in range(tam):
    num = int(input('Digite um nº: '))
    vetor1.append(num)

print('vetor 2')
for i in range(tam):
    num = int(input('Digite um nº: '))
    vetor2.append(num)

print('vetor 3')
for i in range(tam):
    num = int(input('Digite um nº: '))
    vetor3.append(num)

composto = []
for i in range(tam):
    composto.append(vetor1[i])
    composto.append(vetor2[i])
    composto.append(vetor3[i])

print('Composto: {}'.format(composto))