# author: Christian Alves
# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input('Digite um número: '))

a, b = 1, 1
for i in range(0, n):
    print(a, end=' ')
    a, b = b, a+b
print()