# author: Christian Alves
# Altere o programa anterior para mostrar no final a soma dos números.

soma = 0
for i in range(int(input('Digite um número: ')), int(input('Digite um número: ')) + 1):
    soma += i
print('Soma: {}'.format(soma))