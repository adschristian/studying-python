# author: Christian Alves
# Classe Quadrado: Crie uma classe que modele um quadrado:
# a. Atributos: Tamanho do lado
# b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:

    def __init__(self, lado):
        assert isinstance(lado, float)
        self.__lado = lado
    
    def setLado(self, lado):
        assert isinstance(lado, float)
        self.__lado = lado
    
    def getLado(self):
        return self.__lado
    
    def getArea(self):
        return self.__lado*self.__lado
