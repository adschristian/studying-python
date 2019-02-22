# author: Christian Alves
# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
'''
"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
'''
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
'''
Sistema Operacional         Votos           %
-------------------         -----           ---
Windows Server               1500           17%
Unix                         3500           40%
Linux                        3000           34%
Netware                       500            5%
Mac OS                        150            2%
Outro                         150            2%
-------------------         -----
Total                        8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''

import os

opcoes = '1) Windows Server\n2) Unix\n3) Linux\n4) Netware\n5) Mac OS\n6) Outro\n0) Fechar'
so = {'Windows Server': 0, 'Unix': 0, 'Linux': 0, 'Netware': 0, 'Mac OS': 0, 'Outro': 0}

while True:
    print('"Qual o melhor Sistema Operacional para uso em servidores?\n')
    print(opcoes)
    op = input('Voto: ')
    if op == '0':
        os.system('clear')
        break
    
    if op == '1':
        so['Windows Server'] += 1
    elif op == '2':
        so['Unix'] += 1
    elif op == '3':
        so['Linux'] += 1
    elif op == '4':
        so['Netware'] += 1
    elif op == '5':
        so['Mac OS'] += 1
    elif op == '6':
        so['Outro'] += 1
    else:
        print('Opção invalida. Pressione [Enter] para continuar')
        input()
    
    os.system('clear')

total = sum(so.values())

for sistema, votos in so.items():
    porcentagem = votos*100/total
    print('{:>20} {:>10} {:>10}'.format(sistema, votos, round(porcentagem)))
else:
    print('Total: {:>30}\n'.format(total))

mais_votado = max(so, key=so.get)
quantidade = so[mais_votado]
porcentagem = quantidade*100/total

print('O Sistema Operacional mais votado foi o {}, com {} votos, correspondendo a {}% dos votos.'.format(mais_votado, quantidade, round(porcentagem)))