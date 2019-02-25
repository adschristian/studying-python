# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar um arquivo, chamado "usuarios.txt".
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt".
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

def to_mega(value):
    assert isinstance(value, int)
    return value/1024**2

def porcentagem(total, parte):
    assert isinstance(total, float)
    assert isinstance(parte, float)
    return parte*100/total

from os import system

arq = open('arquivos/usuarios.txt', 'r')
linhas = arq.readlines()
arq.close()

usuarios = {}
for linha in linhas:
    user = linha[:15].strip()
    size = linha[15:].strip()
    usuarios[user] = to_mega(int(size))

print('{:<25}{}'.format('ACME Inc.', 'Uso do espaço em disco pelos usuários'))
print(75*'-')

print('{:^5}{:<15}{:^15}{:>15}\n'.format('Nr.', 'Usuário', 'Espaço utilizado', '% do uso'))

formato = '{:<5}{:<15}{:>15} MB{:>12}%'

num = 1
espaco_total = sum(usuarios.values())
for nome, espaco in usuarios.items():
    p = porcentagem(espaco_total, espaco)
    print(formato.format(num, nome, round(espaco, 2), round(p, 2)))
    num += 1
else:
    print()

print('Espaço total ocupado: {} MB'.format(round(espaco_total, 2)))
print('Espaço médio ocupado: {} MB'.format(round(espaco_total/len(usuarios), 2)))