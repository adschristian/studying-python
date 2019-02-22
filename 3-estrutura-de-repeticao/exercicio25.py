# author: Christian Alves
#  Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n = int(input('Nº de alunos: '))
soma = 0
for i in range(n):
    soma += int(input('Idade: '))

media = soma/n
if media >= 60:
    print('Mais de 60 anos')
elif media >= 26:
    print('De 26 e 60 anos')
else:
    print('De 0 e 25 anos')

print('Média de: {}'.format(round(media, 2)))