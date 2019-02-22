# author: Christian Alves
# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

nome = input('Digite seu nome: ')
for i in range(len(nome), 0, -1):
    print(nome[0:i])