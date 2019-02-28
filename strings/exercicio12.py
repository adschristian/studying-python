# author: Chritian Alves
# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

import re

def validatelefone(telefone):
    assert isinstance(telefone, str)
    padrao = '[0-9]{3}[\\-]?[0-9]{4}|[0-9]{4}[\\-]?[0-9]{4}'
    regex = re.compile(padrao)
    return True if regex.match(padrao) else False

def corrigetelefone(telefone):
    assert isinstance(telefone, str)

    if not validatelefone(telefone):
        return 'Telefone inválido'

    msg = 'Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.'
    if telefone.strip().count('-') == 1 and len(telefone.strip()) == 8:
        print(msg)
        telefone = '3{}'.format(telefone)
    elif telefone.strip().count('-') == 0 and len(telefone.strip()) == 7:
        print(msg)
        telefone = '3{}'.format(telefone)
    return telefone

def main():
    telefone = input('Digite um telefone: ')
    print(corrigetelefone(telefone))

if __name__=='__main__':
    main()