# author: Christian Alves
# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
## Média de Aproveitamento       Conceito
## Entre 9.0 e 10.0              A
## Entre 7.5 e 9.0               B
## Entre 6.0 e 7.5               C
## Entre 4.0 e 6.0               D
## Entre 4.0 e zero              E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input('1ª Nota: '))
nota2 = float(input('2ª Nota: '))

media = (nota1+nota2)/2

print('1º semestre: {}'.format(round(nota1, 2)))
print('2º semestre: {}'.format(round(nota2, 2)))
print('Média: {}'.format(round(media, 2)))

if media >= 9:
    print('Conceito: A')
elif media >= 7.5:
    print('Conceito: B')
elif media >= 6:
    print('Conceito: C')
elif media >= 4:
    print('Conceito: D')
else:
    print('Conceito: E')

print('Aprovado' if media >= 6 else 'Reprovado')