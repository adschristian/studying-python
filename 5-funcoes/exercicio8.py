# author: Christian Alves
# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def numberlen(numero):
    assert isinstance(numero, int)
    return len(str(numero))

num = int(input('Digite um nº: '))
quant = numberlen(num)
print('{} caractere(s)'.format(quant))