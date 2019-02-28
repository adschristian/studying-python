# author: Christian Alves
# Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

pessoas = list()

for i in range(5):
    idade = int(input('Idade: '))
    altura = int(input('Altura (cm): '))
    pessoas.append(tuple((idade, altura)))

print(pessoas[::-1])