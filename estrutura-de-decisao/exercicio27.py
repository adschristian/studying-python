# author: Christian Alves
# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
##                  Até 5 kg            Acima de 5 kg
## Morango          R$ 2,50/kg          R$ 2,20/kg
## Maçã             R$ 1,50/kg          R$ 1,50/kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = int(input('Morango (Kg): '))
maca = int(input('Maçã (Kg): '))
total = 0

if morango > 5:
    total += 2.2 * morango
else:
    total += 2.5 * morango

if maca > 5:
    total += 1.5 * maca
else:
    total += 1.8 * maca

if morango+maca > 8 or total > 25:
    print('-10%')
    total -= total*0.1

print('Valor total: R$ {}'.format(round(total, 2)))