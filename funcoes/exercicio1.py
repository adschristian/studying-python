# author: Christian Alves
# Faça um programa para imprimir:
'''
1
2 2
3 3 3
.....
n n n n n n ... n
'''
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.


def imprimir(n):
    '''
    1
    2 2
    3 3 3
    .....
    n n n n n n ... n
    '''
    
    assert isinstance(n, int)
    for i in range(1, n+1):
        print('{}'.format((str(i)+' ')*i))
    else:
        print()


numero = int(input('Digite um nº: '))
imprimir(numero)