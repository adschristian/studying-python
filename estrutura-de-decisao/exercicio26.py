# author: Christian Alves
# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
## a. Álcool:
## b. até 20 litros, desconto de 3% por litro
## c. acima de 20 litros, desconto de 5% por litro
## d. Gasolina:
## e. até 20 litros, desconto de 4% por litro
## f. acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

GASOLINA = 2.5
ALCOOL = 1.9

litros = int(input('Quantos litros? '))
print('A) álcool\nB) gasolina')
tipo = input('Selecione uma opção: ').lower()

valor = 0
if tipo == 'a':
    if litros > 20:
        valor = litros * (ALCOOL * 0.95)
    else:
        valor = litros * (ALCOOL * 0.97)
elif tipo == 'b':
    if litros > 20:
        valor = litros * (ALCOOL * 0.94)
    else:
        valor = litros * (ALCOOL * 0.96)
else:
    print('Opção inválida.')
    exit()

print('Total: R$ {}'.format(round(valor, 2)))