# author: Christian Alves
# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

from os import system

def valorPagamento(valor, atraso):
    assert isinstance(valor, float)
    assert isinstance(atraso, int)
    '''
    função que retorna o valor a ser pago de uma prestação
    '''
    acrescimo = (valor*0.03)+(valor*0.001*atraso)
    return valor+acrescimo if atraso>0 else valor

pagamentos = []

while True:
    print('Pressione [0] para fechar')
    prestacao = float(input('Valor da prestação ($): '))
    if prestacao == 0:
        break
    dias = int(input('Dias de atraso: '))
    system('clear')
    total = valorPagamento(prestacao, dias)
    print('Total a pagar: $ {}'.format(round(total, 2)))
    pagamentos.append(total)

system('clear')

print('Relatório')
print('Total de pagamentos efetuados: {}'.format(len(pagamentos)))
print('Valor total pago: $ {}'.format(round(sum(pagamentos), 2)))