# author: Christian Alves
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(a, b, c):
    '''
    return a+b+c
    '''
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert isinstance(c, int)

    return a+b+c

num1 = int(input('Digite um nº: '))
num2 = int(input('Digite um nº: '))
num3 = int(input('Digite um nº: '))
print('Soma = {}'.format(soma(num1, num2, num3)))