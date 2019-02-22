# author: Christian Alves
# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
## Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;## Triângulo Equilátero: três lados iguais;
## Triângulo Isósceles: quaisquer dois lados iguais;
## Triângulo Escaleno: três lados diferentes;

a = int(input('Lado: '))
b = int(input('Lado: '))
c = int(input('Lado: '))

if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        print('Triângulo equilátero')
    elif a!=b and b!=c and a!=c:
        print('Triângulo escaleno')
    else:
        print('Triângulo isósceles')
else:
    print('Não forma triângulo')