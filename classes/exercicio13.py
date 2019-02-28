# Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário.
# Escreva um pequeno programa que teste sua classe.

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

def main():
    func = Funcionario('Digerson', 2129.)
    print('Nome: {}'.format(func.nome()))
    print('Salário: R$ {}'.format(round(func.salario(), 2)))

if __name__=='__main__':
    main()

