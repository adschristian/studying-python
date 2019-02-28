# author: Christian Alves
# Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.

class Funcionario:
    def __init__(self, nome, salario):
        assert isinstance(nome, str)
        assert isinstance(salario, float)
        self.__nome = nome
        self.__salario = salario
    
    def nome(self):
        return self.__nome
    
    def salario(self):
        return self.__salario
    
    def aumentarSalario(self, percentual):
        assert isinstance(percentual, float)
        aumento = self.__salario*percentual/100
        self.__salario += aumento

def main():
    func = Funcionario('Digerson', 1000.)
    print('Nome: {}'.format(func.nome()))
    print('Salário: R$ {}'.format(round(func.salario(), 2)))
    func.aumentarSalario(10.)
    print('Salário: R$ {}'.format(round(func.salario(), 2)))


if __name__=='__main__':
    main()
