# author: Christian Alves
# Faça um programa que leia e valide as seguintes informações:
## a. Nome: maior que 3 caracteres;
## b. Idade: entre 0 e 150;
## c. Salário: maior que zero;
## d. Sexo: 'f' ou 'm';
## e. Estado Civil: 's', 'c', 'v', 'd';

nome = input('Nome: ')
while not len(nome) > 3:
    print('Precisa ter mais de 3 caracteres')
    nome = input('Nome: ')

idade = int(input('Idade (entre 0 e 150): '))
while idade > 150 or idade < 0:
    idade = int(input('Idade: '))

salario = float(input('Salário ($): '))
while not salario > 0:
    salario = float(input('Salário ($): '))

sexo = input('Sexo (m/f): ')
while sexo not in ('m', 'f'):
    sexo = input('Sexo (m/f): ')

eCivil = input('Estado civil (s/c/v/d): ')
while eCivil not in ('s','c','v','d'):
    eCivil = input('Estado civil (s/c/v/d): ')