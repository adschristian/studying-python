# author: Christian Alves
# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.

num = int(input('Digite um nº: '))
for i in range(1, 11):
    print('{} x {} = {}'.format(num, i, (num*i)))