# author: Christian Alves
# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
## a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
## b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
## c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
## d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = float(input('Valor de a: '))
if a==0:
	print('Não é uma equação do segundo grau')
	exit()
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

delta = (b**2)-(4*a*c)
if delta < 0:
	print('A equação não possui raízes reais')
	exit()

x1 = (-b+delta)/2*a
if delta == 0:
	print('x = {}'.format(x1))
	exit()

x2 = (-b-delta)/2*a
print('x1 = {}\nx2 = {}'.format(x1, x2))
