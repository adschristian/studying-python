# author: Christian Alves
# Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

TAM = 3

medias = []
for i in range(TAM):
    print('Aluno {}: '.format(i+1))
    soma = 0
    for i in range(4):
        nota = float(input('{}ª nota: '.format(i+1)))
        soma += nota
    media = soma/4
    medias.append(media)

def aprovados(x):
    return x >= 7

quantidade = len(list(filter(aprovados, medias)))

print('Aprovados: {} alunos'.format(quantidade))