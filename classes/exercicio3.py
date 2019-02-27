# author: Christian Alves
# Classe Retangulo: Crie uma classe que modele um retangulo:
# a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:

    def __init__(self, comprimento, largura):
        assert isinstance(comprimento, float)
        assert isinstance(largura, float)
        
        self.__comprimento = comprimento
        self.__largura = largura

    def setComprimento(self, comprimento):
        assert isinstance(comprimento, float)
        self.__comprimento = comprimento
    
    def getComprimento(self):
        return self.__comprimento
    
    def setLargura(self, largura):
        assert isinstance(largura, float)
        self.__largura = largura
    
    def getLargura(self):
        return self.__largura
    
    def area(self):
        return self.__comprimento*self.__largura
    
    def perimetro(self):
        return 2*(self.__comprimento+self.__largura)

def main():
    medidas = None
    comp = float(input('Digite o comprimento (m): '))
    larg = float(input('Digite a largura (m): '))
    
    medidas = Retangulo(comp, larg)

    area = medidas.area()
    rodape = medidas.perimetro()
    saida = 'Serão necessários {}m² de piso, e {}m de rodapé.'
    print(saida.format(area, rodape))

if __name__=='__main__':
    main()