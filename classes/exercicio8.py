# author: Christian Alves
# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:

    def __init__(self, nome):
        assert isinstance(nome, str)
        self.__nome = nome
        self.__bucho = list()
    
    def comer(self, comida):
        self.__bucho.append(comida)

    def digerir(self):
        return None if len(self.__bucho)==0 else self.__bucho.pop(0)

    def verBucho(self):
        bucho = 'Bucho do {}\n'.format(self.__nome)
        for comida in self.__bucho:
            bucho += '{}\n'.format(comida)
        return bucho
    
    def __str__(self):
        return 'Macaco {}'.format(self.__nome)
    
def main():
    monkey1 = Macaco('twelves')
    monkey2 = Macaco('champignon')

    monkey1.comer('banana')
    monkey1.comer('pera')
    monkey1.comer('abacate')
    print(monkey1.verBucho())

    monkey2.comer('maçã')
    monkey2.comer('abacaxi')
    monkey2.comer('melão')
    print(monkey2.verBucho())

    monkey2.digerir()

    monkey2.comer(monkey1)

    print(monkey2.verBucho())

if __name__=='__main__':
    main()