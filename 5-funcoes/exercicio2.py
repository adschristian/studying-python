# author: Christian Alves
# Faça um programa para imprimir:
'''
1
1 2
1 2 3
.....
1 2 3 ... n
'''
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimir(n):
    '''
    1
    1 2
    1 2 3
    .....
    1 2 3 ... n
    '''

    assert isinstance(n, int)
    
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(str(j) + ' ', end='')
        else:
            print()

numero = int(input('Digite um nº: '))
imprimir(numero)