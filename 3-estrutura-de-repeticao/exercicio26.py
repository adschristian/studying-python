# author: Christian Alves
# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input('Nº de eleitores: '))
a = b = c = 0
for eleitor in range(eleitores):
    print('1) Candidato A\n2) Candidato B\n3) Candidato C')
    voto = input('Candidato: ')
    if voto == '1':
        a += 1
    elif voto == '2':
        b += 1
    elif voto == '3':
        c += 1

print('Candidato A: {} votos'.format(a))
print('Candidato B: {} votos'.format(b))
print('Candidato C: {} votos'.format(c))