# author: Christian Alves
# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

n = int(input('Digite um nº: '))

soma = 0
m = 1
print('S = ', end='')
for i in range(1, n+1):
    soma += i/m
    print('{}/{}'.format(i, m), end='')
    if i < n:
        print(' + ', end='')
        m += 2

print(' = {}'.format(round(soma, 3)))