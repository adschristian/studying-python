# author: Christian Alves
# Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
# Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento:

    def __init__(self, saldo=0., taxa=0.):
        self.__saldo = saldo
        self.__taxaJuros = taxa

    def adicionaJuros(self):
        juros = self.__saldo*self.__taxaJuros/100
        self.__saldo += juros
    
    def saldo(self):
        return self.__saldo
    

def main():
    conta = ContaInvestimento(1000, 10)
    conta.adicionaJuros()
    conta.adicionaJuros()
    conta.adicionaJuros()
    conta.adicionaJuros()
    conta.adicionaJuros()
    print('Saldo: R$ {}'.format(round(conta.saldo(), 2)))

if __name__=='__main__':
    main()