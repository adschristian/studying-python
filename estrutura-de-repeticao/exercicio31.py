# author: Christian Alves
# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

while True:
    total = 0
    count = 1
    while True:
        preco = float(input('Produto {}: '.format(count)))
        total += preco
        count += 1
        if preco == 0:
            print('Total: $ {}'.format(round(total, 2)))
            dinheiro = float(input('Dinheiro ($): '))
            troco = dinheiro-total
            print('Troco: $ {}'.format(round(troco, 2)))
            break
        elif preco < 0:
            print('Fechando o programa...')
            exit()