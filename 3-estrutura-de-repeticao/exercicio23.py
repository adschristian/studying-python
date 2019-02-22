# author: Christian Alves
# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input('Digite um nº: '))
primos = list()
divisoes = 0
for numero in range(1, n+1):
    primo = True
    
    if numero == 2:
        primos.append(numero)
        continue
    
    if numero < 2 or numero%2 == 0:
        continue

    div = 3
    
    while div <= numero//2:
        if numero%div == 0:
            primo = False
        div += 2
    if primo:
        primos.append(numero)

print('Primos: {}'.format(primos))