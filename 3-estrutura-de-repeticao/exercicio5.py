# author: Christian Alves
# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

A = int(input('População da cidade A: '))
while not A > 0:
    A = int(input('População da cidade A: '))

taxa_cidadeA = float(input('Taxa de crescimento (%): '))
while not taxa_cidadeA > 0:
    taxa_cidadeA = float(input('Taxa de crescimento (%): '))

B = int(input('População da cidade B: '))
while not B > 0:
    B = int(input('População da cidade B: '))

taxa_cidadeB = float(input('Taxa de crescimento (%): '))
while not taxa_cidadeB > 0:
    taxa_cidadeB = float(input('Taxa de crescimento (%): '))

anos = 0
while A < B:
    A = A + (A*taxa_cidadeA/100)
    B = B + (B*taxa_cidadeB/100)
    anos += 1

print('Depois de {} anos, a cidade A ultrapassa a população da cidade B'.format(anos))
print('A: {} habitantes\nB: {} habitantes'.format(round(A), round(B)))