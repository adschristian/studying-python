# author: Christian Alves
# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

from os import system

def horario(hora, minuto):
    assert isinstance(hora, int)
    assert isinstance(minuto, int)
    assert hora>=0 and hora<24
    assert minuto>=0 and minuto<60
    
    auxHora = hora
    periodo = None
    if hora == 0:
        auxHora == 12
        periodo = 'A.M.'
    elif hora == 12:
        periodo = 'P.M.'
    else:
        auxHora = hora%12
        if hora > 12:
            periodo = 'P.M.'
        else:
            periodo = 'A.M.'
    
    return '{:0>2}:{:0>2} {}'.format(auxHora, minuto, periodo)

while True:
    print('Tecle [Enter] para sair')
    hora = input('Hora: ')
    if hora.strip() == '':
        break
    min = input('Minuto: ')
    if min.strip() == '':
        break
    
    if hora.isnumeric() and min.isnumeric:
        system('clear')
        print('{}\n'.format(horario(int(hora), int(min))))
    else:
        print('Valores inválidos.')