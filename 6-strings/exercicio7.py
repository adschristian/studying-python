# author: Christian Alves
# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# a. quantos espaços em branco existem na frase.
# b. quantas vezes aparecem as vogais a, e, i, o, u.

frase = input('Digite uma frase: ')
aux = frase.lower()
espacos = aux.count(' ')
a = aux.count('a')
e = aux.count('e')
i = aux.count('i')
o = aux.count('o')
u = aux.count('u')

print('Espaços: {}'.format(espacos))
print('Vogal a: {}'.format(a))
print('Vogal e: {}'.format(e))
print('Vogal i: {}'.format(i))
print('Vogal o: {}'.format(o))
print('Vogal u: {}'.format(u))