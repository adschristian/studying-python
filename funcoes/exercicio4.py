# author: Christian Alves
# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def positiveOrNegative(n):
    '''
    retorna 'P', se n for positivo
    retorna 'N', se n for negativo
    '''
    assert isinstance(n, int)

    return 'P' if n > 0 else 'N'

numero =  int(input('Digite um nº: '))
print(positiveOrNegative(numero))