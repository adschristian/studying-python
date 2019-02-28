# author: Christian Alves
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = int(input('Nº de iterações: '))

num = int(input('Digite um nº: '))

while num >= 1000 or num <= 0:
    num = int(input('Digite um nº: '))
maior = menor = soma = num

for i in range(1, n):
    num = int(input('Digite um nº: '))
    while num >= 1000 or num <= 0:
        num = int(input('Digite um nº: '))
    if num > maior: maior = num
    elif num < menor: menor = num
    soma += num

print('Maior: {:>2}'.format(maior))
print('Menor: {:>2}'.format(menor))
print('Soma:  {:>2}'.format(soma))
