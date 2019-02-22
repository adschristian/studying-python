# author: Christian Alves
# Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
## 326 = 3 centenas, 2 dezenas e 6 unidades
## 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = int(input('Digite um nº (<1000): '))
if numero >= 1000: exit()

print('{}'.format(numero))
if numero > 100:
    centenas = numero//100
    numero -= centenas*100
    print('{} centena(s)'.format(centenas))
if numero > 10:
    dezenas = numero//10
    numero -= dezenas*10
    print('{} dezena(s)'.format(dezenas))
if numero > 0:
    unidades = numero%10
    print('{} unidade(s)'.format(unidades))
