# author: Christian Alves
# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# a. Maior e Menor Acerto;
# b. Total de Alunos que utilizaram o sistema;
# c. A Média das Notas da Turma.

from os import system

gabarito = list()

print('Gabarito')
for i in range(10):
    resposta = input('Questão {} (a/b/c/d/e): '.format(i+1)).lower()
    while resposta not in ('a','b','c','d','e'):
        resposta = input('Questão {} (a/b/c/d/e): '.format(i+1)).lower()
    gabarito.append(resposta)
    system('clear')

system('clear')

alunos = dict()
while True:
    print('(x + Enter): terminar aplicação e gerar relatório')
    nome = input('Nome completo do aluno: ').lower()
    if nome == 'x':
        break
    
    nota = 0
    print('Respostas da prova')
    for i in range(10):
        resposta = input('Questão {} (a/b/c/d/e): '.format(i+1)).lower()
        while resposta not in ('a','b','c','d','e'):
            resposta = input('Questão {} (a/b/c/d/e): '.format(i+1)).lower()
        if resposta == gabarito[i]:
            nota += 1
    
    alunos[nome] = nota
    system('clear')

system('clear')
print('Relatório')

print('Maior nota: {}'.format(max(alunos.values())))
print('Menor nota: {}'.format(min(alunos.values())))
print('Total de alunos: {}'.format(len(alunos)))
mediaNotas = sum(alunos.values())/len(alunos)
print('Média das notas: {}'.format(mediaNotas))