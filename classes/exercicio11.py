# author: Christian Alves
# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
# a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
# b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
# c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
# d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
# e. Forneça um método adicionarGasolina( ), para abastecer o tanque.

class Carro:

    def __init__(self, consumo):
        self.__consumo = consumo
        self.__tanque = 0
    
    def andar(self, distancia):
        assert isinstance(distancia, (int, float))
        litros = distancia/self.__consumo
        if litros > self.__tanque:
            print('Combustível insuficiente!')
        else:
            self.__tanque -= litros
    
    def totalCombustivel(self):
        return self.__tanque
    
    def adicionarCombustivel(self, litros):
        assert isinstance(litros, (int, float))
        self.__tanque += litros

def main():
    carro = Carro(9)
    carro.andar(21.6)
    carro.adicionarCombustivel(32)
    carro.andar(45.98)
    print(round(carro.totalCombustivel(), 2))

if __name__=='__main__':
    main()