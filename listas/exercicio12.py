# author: Christian Alves
# Foram anotadas as idades e alturas de 30 alunos. Faça um programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

alunos = []

tam = 5

soma_altura = 0
for i in range(tam):
    idade = int(input('Idade: '))
    altura = float(input('Altura (m): '))
    soma_altura += altura
    alunos.append(tuple((idade, altura)))

media_altura = soma_altura/len(alunos)

count = 0
for aluno in alunos:
    if aluno[0] > 13 and aluno[1] > media_altura:
        count += 1

print('{} alunos'.format(count))