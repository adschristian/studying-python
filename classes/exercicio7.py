# author: Christian Alves
# Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# a. Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

from datetime import datetime

class Tamagushi:

    __MAX = 100
    __MIN = 0

    def __init__(self, nome):
        assert isinstance(nome, str)
        self.__nome = nome
        self.__fome = self.__MAX
        self.__saude = self.__MAX
        self.__idade = 0
    
    def alternarNome(self, nome):
        assert isinstance(nome, str)
        self.__nome = nome
    
    def nome(self):
        return self.__nome
    
    def alterarFome(self, fome):
        assert isinstance(fome, int)
        if fome > self.__MAX:
            self.__fome = self.__MAX
        elif fome < self.__MIN:
            self.__fome = self.__MIN
        else:
            self.__fome = fome
    
    def fome(self):
        return self.__fome
    
    def alternarSaude(self, saude):
        assert isinstance(saude, int)
        if saude > self.__MAX:
            self.__saude = self.__MAX
        elif saude < self.__MIN:
            self.__saude = self.__MIN
        else:
            self.__saude = saude
    
    def saude(self):
        return self.__saude

    def alternarIdade(self, idade):
        assert isinstance(idade, int)
        self.__idade = idade
    
    def idade(self):
        return self.__idade
    
    def humor(self):
        return (self.__fome+self.__saude)/2
