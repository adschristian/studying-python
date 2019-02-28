# author: Christian Alves
# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(numero):
    assert isinstance(numero, int)
    return str(numero)[::-1]

numero = int(input('Digite um nº: '))
print('Reverso = {}'.format(reverso(numero)))