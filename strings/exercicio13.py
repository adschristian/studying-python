# author: Christian Alves
# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

from os import system
from random import shuffle, choice

def lerarquivo():
    palavras = None
    try:
        arquivo = open('arquivos/palavras.txt')
        palavras = arquivo.readlines()
        arquivo.close()
    except IOError:
        print('Erro ao abrir o arquivo.')
        exit()
    
    # formatar as palavras da lista, retirando espaços em branco e caracteres de escape
    for i in range(len(palavras)-1):
        palavras[i] = palavras[i].strip()

    return palavras

def embaralha(palavra):
    aux = list(palavra)
    shuffle(aux)
    return ''.join(aux)

def escolherpalavra(lista=[]):
    return choice(lista)

def jogo(palavra):
    assert isinstance(palavra, str)
    
    embaralhada = embaralha(palavra)
    erros = 0
    while erros < 6:
        print('Erros: {}'.format(erros))
        print(embaralhada.upper())
        tentativa = input('Que palavra é essa? ')
        system('clear')
        if tentativa.lower() == palavra:
            print('Você acertou!!')
            print('A palavra é "{}"'.format(palavra.upper()))
            return
        else:
            erros += 1
    else:
        print('Você perdeu!')
        print('A palavra é "{}"'.format(palavra.upper()))

def main():
    lista = lerarquivo()
    endgame = '[Enter] Jogar novamente\n[0] Sair\n'
    while True:
        palavra = escolherpalavra(lista)
        jogo(palavra)
        continua = input(endgame).strip()
        system('clear')
        if continua == '0':
            print('bye')
            exit()
        

if __name__=='__main__':
    main()