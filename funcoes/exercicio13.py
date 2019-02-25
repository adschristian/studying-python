# author: Christian Alves
# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

def desenha(linha=1, coluna=1):
    '''
    desenha um retângula de acordo com o tamanho de linhas e colunas
    '''
    assert isinstance(linha, int)
    assert isinstance(coluna, int)

    if linha > 20:
        linha = 20
    elif linha < 1:
        linha = 1

    if coluna > 20:
        coluna = 20
    elif coluna < 1:
        coluna = 1

    corner = '+'
    line = '--'
    column = '|'
    space = '  '
    
    print(corner, end='')
    for c in range(coluna):
        print(line, end='')
    else:
        print(corner)
    
    for l in range(linha):
        print(column, end='')
        for c in range(coluna):
            print(space, end='')
        else:
            print(column)

    print(corner, end='')
    for c in range(coluna):
        print(line, end='')
    else:
        print(corner)



lines = int(input('nº de linhas: '))
cols = int(input('nº de colunas: '))
desenha(lines, cols)