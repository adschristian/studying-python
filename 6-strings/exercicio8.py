# author: Christian Alves
# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

def palindromo(string):
    '''
    função que retorna se uma sequencia de caracteres é uma frase palíndroma
    '''
    assert isinstance(string, str)
    aux1 = string.upper().replace(' ', '')
    aux2 = aux1[::-1]

    return True if aux1 == aux2 else False

def main():
    string = input('Digite uma frase: ')
    print('É palíndromo' if palindromo(string) else 'Não é palíndromo')

if __name__ == '__main__':
    main()