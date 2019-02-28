# author: Christian Alves
# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class Televisao:

    def __init__(self):
        '''
        canal = 1
        volume = 20
        '''
        self.__canal = 1
        self.__volume = 20

    def aumentar(self):
        if self.__volume < 50:
            self.__volume += 1
        return self.__volume
    
    def diminuir(self):
        if self.__volume > 0:
            self.__volume -= 1
        return self.__volume
    
    def trocacanal(self, canal=None):
        if canal is None:
            if self.__canal+1>100:
                self.__canal = 1
            else:
                self.__canal += 1
        else:
            if canal<=100:
                self.__canal = canal
        
        return self.__canal

def main():
    tv = Televisao()
    print(tv.trocacanal(100))
    print(tv.trocacanal())


if __name__=='__main__':
    main()