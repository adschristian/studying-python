# author: Christian Alves
# Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e __escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

from random import choice
from os import system

class JogoDaForca:

    def __init__(self):
        self.__lista = None
        self.__palavra = None
        self.__amostra = ''
        self.__jafoi = list()
        self.__erros = 0
    
    def __ler(self):
        try:
            arq = open('arquivos/palavras.txt')
            self.__lista = arq.readlines()
            arq.close()
        except IOError:
            print('Erro ao ler arquivo.')
            exit()
    
    def __escolher(self):
        if self.__lista:
            self.__palavra = choice(self.__lista).strip()
            self.__amostra = len(self.__palavra)*'#'
        else:
            return None

    def __tentativa(self, letra):
        self.__jafoi.append(letra)
        indice = self.__palavra.find(letra)
        if indice==-1:
            self.__erros += 1
            return
        
        aux = ''
        for i in range(len(self.__palavra)):
            if self.__palavra[i] == letra:
                aux += letra
            elif self.__amostra[i] != '#':
                aux += self.__amostra[i]
            else:
                aux += '#'
        else:
            self.__amostra = aux

    def __verifica(self):
        return self.__palavra == self.__amostra

    def __mostrarJaFoi(self):
        aux = ''
        for letra in self.__jafoi:
            aux += '{} '.format(letra)
        return aux
    
    def jogo(self):
        # inicializando o jogo
        self.__ler()
        self.__escolher()

        print('Jogo da forca')
        while self.__erros<6:
            print('Erros: {}'.format(self.__erros))
            print('A palavra é: {}'.format(self.__amostra))
            print('Já foi: {}'.format(self.__mostrarJaFoi()))
            letra = input('Digite uma letra: ')
            system('clear')
            self.__tentativa(letra)
            if self.__verifica():
                print('Você venceu!!')
                return
        
        print('Você perdeu!!')
        print('A palavra é: {}'.format(self.__palavra))

def main():
    while True:
        forca = JogoDaForca()
        forca.jogo()
        op = input('[Enter] Continuar\n[0] Sair\nOpção: ')
        if op == '0':
            exit()
        system('clear')

if __name__=='__main__':
    main()