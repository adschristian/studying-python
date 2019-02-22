# Faça um programa que peça dois números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo.
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

num1 = int(input('Type a int number: '))
num2 = int(input('Type another int number: '))
num3 = float(input('Type a double number: '))

a = (num1*2)*(num2/2)
b = (num1*3)+num3
c = num3**3

print('a) {}\nb) {}\nc) {}'.format(a, b, c))