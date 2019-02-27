# Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
# a. Possua uma classe chamada Ponto, com os atributos x e y.
# b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
# c. Possua uma função para imprimir os valores da classe Ponto
# d. Possua uma função para encontrar o centro de um Retângulo.
# e. Você deve criar alguns objetos da classe Retangulo.
# f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
# g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
# h. O valor do centro do objeto deve ser mostrado na tela
# i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x, y):
        assert isinstance(x, (float, int))
        assert isinstance(y, (float, int))
        self.__x = x
        self.__y = y
    
    def pontos(self):
        '''
        pontos() -> x, y
        '''
        return self.__x, self.__y
    
    def __str__(self):
        saida = 'x = {}, y = {}'
        return saida.format(self.__x, self.__y)

class Retangulo:
    def __init__(self, altura, largura):
        assert isinstance(altura, Ponto)
        assert isinstance(largura, Ponto)
        self.__altura = altura
        self.__largura = largura
    
    def centro(self):
        '''
        centro() -> Ponto(x/2, y/2)
        '''
        ax, ay = self.__largura.pontos()
        largura = abs(ax-ay)
        lx, ly = self.__altura.pontos()
        altura = abs(ly-lx)
        centro = Ponto(altura/2, largura/2)
        return centro

def main():
    altura = Ponto(0, 8)
    largura = Ponto(3, 0)
    
    retangulo = Retangulo(altura, largura)

    print(retangulo.centro())

if __name__=='__main__':
    main()