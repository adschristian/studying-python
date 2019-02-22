# author: Christian Alves
# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

def bissexto(ano):
        return True if ano%400==0 or ano%4==0 and ano%100!=0 else False

def __validarData(data):
    '''
    verifica se 'data' está no formato dd/MM/yyyy
    '''
    assert isinstance(data, str)
    aux = data.split('/')
    
    if len(aux) != 3:
        return False
    
    dia = aux[0]
    mes = aux[1]
    ano = aux[2]
    
    if dia.isnumeric():
        dia = int(dia)
    else:
        return False

    if mes.isnumeric():
        mes = int(mes)
    else:
        return False
    
    if ano.isnumeric():
        ano = int(ano)
    else:
        return False

    if mes in (1,3,5,7,8,10,12):
        if dia > 31 or dia < 1:
            return False
    elif mes in (4,6,9,11):
        if dia > 31 or dia < 1:
            return False
    elif mes == 2:
        if bissexto(ano):
            if dia > 29 or dia < 1:
                return False
        else:
            if dia > 28 or dia < 1:
                return False
    else:
        return False
    
    return True

def mesPorExtenso(data):
    assert isinstance(data, str)
    if not __validarData(data):
        return 'NULL'
    
    dia, mes, ano = data.split('/')

    return '{} de {} de {}'.format(dia, meses[int(mes)-1].capitalize(), ano)


data = input('Digite uma data (dd/MM/yyyy): ')
print(mesPorExtenso(data))