# author: Christian Alves
# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios

class ContaCorrente:
    
    def __init__(self, numero, nome, saldo=0.):
        '''
        numero = número da conta
        nome = nome do correntista
        saldo = saldo inicial (por padrão é zero)
        '''
        assert isinstance(numero, int)
        assert isinstance(nome, str)
        assert isinstance(saldo, float)
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
    
    def alterarnome(self, nome):
        self.__nome = nome
    
    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def sacar(self, valor):
        if self.__saldo-valor<0:
            return False
        self.__saldo -= valor
        return self.__saldo
    
