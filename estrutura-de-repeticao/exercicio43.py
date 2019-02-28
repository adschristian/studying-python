# author: Christian Alves
# O cardápio de uma lanchonete é o seguinte:
'''
Especificação       Código          Preço
Cachorro Quente         100       R$ 1,20
Bauru Simples           101       R$ 1,30
Bauru com ovo           102       R$ 1,50
Hambúrguer              103       R$ 1,20
Cheeseburguer           104       R$ 1,30
Refrigerante            105       R$ 1,00
'''
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que   cliente deve informar quando o pedido deve ser encerrado.

total = 0
while True:
    codigo = input('Código: ')

    if codigo == 'f':
        break
    if codigo not in ('100', '101', '102', '103', '104', '105'):
        print('Código não encontrado.')
        continue

    quantidade = int(input('Quantidade: '))
    preco = 0

    if codigo == '100':
        preco = 1.2
    elif codigo == '101':
        preco = 1.3
    elif codigo == '102':
        preco = 1.5
    elif codigo == '103':
        preco = 1.2
    elif codigo == '104':
        preco = 1.3
    else:
        preco = 1
    total += quantidade*preco
    print('{} x R$ {} = R$ {}'.format(quantidade, preco, round(quantidade*preco, 2)))

print('Total a pagar: R$ {}'.format(round(total, 2)))