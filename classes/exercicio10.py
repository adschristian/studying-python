# author: Christian Alves
# Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
# a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
## i. tipoCombustivel.
## ii. valorLitro
## iii. quantidadeCombustivel
# b. Possua no mínimo esses métodos:
## i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
## ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
## iii. alterarValor( ) – altera o valor do litro do combustível.
## iv. alterarCombustivel( ) – altera o tipo do combustível.
## v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class Bomba:
    def __init__(self, tipo, valor, litros=500.):
        assert isinstance(tipo, str)
        assert isinstance(valor, float)
        assert isinstance(litros, (float, int))
        self.__tipo = tipo
        self.__valor = valor
        self.__litros = litros
    
    def abastecerPorValor(self, valor):
        assert isinstance(valor, float)
        litros = valor/self.__valor
        if litros > self.__litros:
            troco = (litros-self.__litros)*self.__valor
            aux, self.__litros = self.__litros, 0
            print('Troco: R$ {}'.format(troco))
            return aux
        else:
            self.__litros -= litros
            return litros
    
    def abastecerPorLitro(self, litros):
        assert isinstance(litros, (float, int))
        if litros > self.__litros:
            aux, self.__litros = self.__litros, 0
            return aux*self.__valor
        else:
            self.__litros -= litros
            return litros*self.__valor
    
    def alterarValor(self, valor):
        assert isinstance(valor, float)
        self.__valor = valor
    
    def alterarCombustivel(self, tipo):
        assert isinstance(str)
        self.__tipo = tipo
    
    def alterarQuantidade(self, litros):
        assert isinstance(litros, (float, int))
        self.__litros = litros


def main():
    bomba = Bomba('gasolina', 3.59, 674)
    print('Total a pagar: R$ {}'.format(round(bomba.abastecerPorLitro(30), 2)))
    print('Total: {} litros'.format(round(bomba.abastecerPorValor(50.), 2)))
    
if __name__=='__main__':
    main()