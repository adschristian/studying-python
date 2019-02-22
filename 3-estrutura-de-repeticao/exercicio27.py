# author: Christian Alves
# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input('Nº de turmas: '))

alunos = 0
for turma in range(turmas):
    alunos += int(input('Nº de alunos: '))

media = alunos/turmas
print('Média de alunos/turma = {}'.format(media))