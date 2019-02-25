# author: Christian Alves
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
##                  Até 5 kg            Acima de 5 kg
## Filé duplo       R$ 4,90/kg          R$ 5,80/kg
## Alcatra          R$ 5,90/kg          R$ 6,80/kg
## Picanha          R$ 6,90/kg          R$ 7,80/kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print('a) Filé duplo\nb) Alcatra\nc) Picanha')
tipo = input('Selecione uma opção: ').lower()
if tipo not in ('a','b','c'):
    print('Opção inválida')
    exit()

kilos = float(input('Kg: '))

cartao = False
if input('Pagamento no cartão Tabajara? (s/n)').lower() == 's':
    cartao = True

total = 0

print(2*'\n')
print('Informações da compra')
print('Produto: ', end='')
if tipo == 'a':
    print('Filé duplo')
    if kilos > 5:
        total = kilos * 5.8
    else:
        total = kilos * 4.9
elif tipo == 'b':
    print('Alcatra')
    if kilos > 5:
        total = kilos * 6.8
    else:
        total = kilos * 5.9
else:
    print('Picanha')
    if kilos > 5:
        total = kilos * 7.8
    else:
        total = kilos * 6.9

print('Preço total: {}'.format(round(total, 2)))

if cartao:
    desconto = round(total*0.05, 2)
    total -= desconto
    print('Desconto: R$ {}'.format(desconto))

print('Total a pagar: R$ {}'.format(round(total, 2)))