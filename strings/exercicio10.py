# author: Christian Alves
# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

unidades = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove')
intermediario = ('onze', 'doze', 'treze', 'catorze', 'quinze',
                 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezenas = ('dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
           'sessenta', 'setenta', 'oitenta', 'noventa')

def porextenso(numero):
    assert isinstance(numero, int)
    saida = '{} = {}'

    if numero < 10:
        return saida.format(numero, unidades[numero])
    elif numero % 10 == 0:
        return saida.format(numero, dezenas[numero//10-1])
    elif numero < 20:
        return saida.format(numero, intermediario[numero % 10-1])
    else:
        d = numero//10
        u = numero % (10*d)
        return '{} = {} e {}'.format(numero, dezenas[d-1], unidades[u])

def main():
    while True:
        numero = input('Digite um nº (n<100): ')
        if not numero.isnumeric():
            print('Tente novamente.',end=' ')
            continue
        if int(numero)>99 or int(numero)<0:
            return
            
        print(porextenso(int(numero)))

if __name__=='__main__':
    main()