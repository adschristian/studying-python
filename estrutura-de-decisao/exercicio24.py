# author: Christian Alves
# Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
## a. par ou ímpar;
## b. positivo ou negativo;
## c. inteiro ou decimal.

a = float(input('Digite um nº: '))
b = float(input('Digite um nº: '))

operacao = input('Digite uma operação (+ - * /): ')
resultado = 0
if operacao == '+':
    print('Soma: {} + {} = '.format(a, b), end='')
    resultado = a+b
elif operacao == '-':
    print('Subtração: {} - {} = '.format(a, b), end='')
    resultado = a-b
elif operacao == '*':
    print('Multiplicação: {} * {} = '.format(a, b), end='')
    resultado = a*b
elif operacao == '/':
    print('Divisão: {} / {} = '.format(a, b), end='')
    if b == 0:
        resultado = 'Indeterminado'
        exit()
    else:
        resultado = a/b
else:
    print('Operação inválida.')
    exit()

print(round(resultado, 4))

print('Par' if resultado%2==0 else 'Ímpar')
print('Negativo' if resultado<0 else 'Positivo')
print('Inteiro' if resultado==round(resultado) else 'Decimal')