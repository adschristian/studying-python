# author: Christian Alves
# Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor

class Bola:

    def __init__(self, cor, circunferencia, material):
        assert isinstance(cor, str)
        assert isinstance(circunferencia, float)
        assert isinstance(material, str)
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material
    
    def trocaCor(self, cor):
        self.__cor = cor
    
    def mostraCor(self):
        return self.__cor

    def __str__(self):
        aux = 'cor: {}\ncircunferencia: {} u.m.\nmaterial: {}'
        return aux.format(self.__cor, self.__circunferencia, self.__material)
