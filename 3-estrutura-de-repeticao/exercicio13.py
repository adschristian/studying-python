# author: Christian Alves
# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input('Digite um nº: '))
exp = int(input('Expoente: '))
resultado = 1

for i in range(0, exp):
    resultado *= base

print('{} ^ {} = {}'.format(base, exp, resultado))