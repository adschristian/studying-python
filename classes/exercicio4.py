# author: Christian Alves
# Classe Pessoa: Crie uma classe que modele uma pessoa:
# a. Atributos: nome, idade, peso e altura
# b. Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        assert isinstance(nome, str)
        assert isinstance(idade, int)
        assert isinstance(peso, float)
        assert isinstance(altura, float)

        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
    
    def envelhecer(self):
        '''
        acrescenta 1 ano à idade
        '''
        if self.__idade < 21:
            self.__altura += 0.5
        self.__idade += 1
        return self.__idade
    
    def engordar(self, kg=1):
        '''
        acrescenta kg ao peso (1kg, por padrão)
        '''
        self.__peso += kg
        return self.__peso
    
    def emagrecer(self, kg=1):
        '''
        decrescenta kg ao peso (1kg, por padrão)
        '''
        self.__peso -= kg
        return self.__peso
    
    def crescer(self, cm=0.5):
        '''
        acrescenta cm à altura (0.5cm, por padrão)
        '''
        self.__altura += cm
        return self.__altura
    
    def __str__(self):
        aux = ''
        aux += 'Nome: {}\n'
        aux += 'Idade: {} anos\n'
        aux += 'Peso: {}kg\n'
        aux += 'Altura: {}cm'
        return aux.format(self.__nome, self.__idade, self.__peso, self.__altura)
    

def main():
    pessoa = Pessoa('christian', 23, 101., 175.)
    print(pessoa)
    pessoa.crescer()
    pessoa.engordar()
    pessoa.envelhecer()
    print(pessoa)

if __name__=='__main__':
    main()