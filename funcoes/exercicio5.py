# author: Christian Alves
# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

from os import system

def somaImposto(taxaImposto, custo):
    assert isinstance(taxaImposto, float)
    assert isinstance(custo, float)

    return custo*(1+(taxaImposto/100))

custo = float(input('Custo ($): '))
taxa = float(input('Taxa (%): '))

system('clear')

novoCusto = somaImposto(taxa, custo)
print('Novo custo: $ {}'.format(round(novoCusto, 2)))