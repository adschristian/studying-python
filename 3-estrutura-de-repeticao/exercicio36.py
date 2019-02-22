# author: Christian Alves
# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo: 
'''
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7
Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
'''

numero = int(input('Montar a tabuada de: '))
inicio = int(input('Começar por: '))
fim = int(input('Terminar em: '))
if fim < inicio:
    print('Valor final não pode ser menor que o valor inicial.')
    exit()
print('Vou montar a tabuada de {0} começando em {1} e terminando em {2}'.format(numero, inicio, fim))

for i in range(inicio, fim+1):
    print('{} x {} = {}'.format(numero, i, (numero*i)))
