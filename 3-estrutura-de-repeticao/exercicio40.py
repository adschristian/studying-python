# author: Christian Alves
# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
'''
a. Nome da cidade;
b. Número de veículos de passeio (em 1999);
c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e. Qual a média de veículos nas cinco cidades juntas;
f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

cidade = input('nome da cidade: ')
veiculos = int(input('nº de veículos: '))
acidentes = int(input('nº de acidentes com vítimas: '))

cidadeMaiorIndice = cidadeMenorIndice = cidade
maiorIndice = menorIndice = acidentes/veiculos

totalVeiculos = veiculos
totalAcidentes = qtdAcidentes = 0

if veiculos < 2000:
    totalAcidentes += acidentes
    qtdAcidentes += 1

for i in range(4):
    cidade = input('nome da cidade: ')
    veiculos = int(input('nº de veículos: '))
    acidentes = int(input('nº de acidentes com vítimas: '))
    
    totalVeiculos += veiculos
    
    media = acidentes/veiculos
    if media > maiorIndice:
        cidadeMaiorIndice = cidade
        maiorIndice = media
    elif media < menorIndice:
        cidadeMenorIndice = cidade
        menorIndice = media
    
    if veiculos < 2000:
        totalAcidentes += acidentes
        qtdAcidentes += 1
    
import os

os.system('clear')

print('relatório\n')

print('maior índice de acidentes')
print('cidade: {}\níndice: {}\n'.format(cidadeMaiorIndice, round(maiorIndice, 3)))
print('menor índice de acidentes')
print('cidade: {}\níndice: {}\n'.format(cidadeMenorIndice, round(menorIndice, 3)))

mediaVeiculos = totalVeiculos/5
print('média de veículos')
print('média: {}'.format(round(mediaVeiculos, 1)))

if qtdAcidentes > 0:
    mediaAcidentes = totalAcidentes/qtdAcidentes
    print('média de acidentes de trânsito nas cidades com menos de 2.000 veículos')
    print('média: {}'.format(round(mediaAcidentes, 1)))