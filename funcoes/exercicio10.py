# author: Christian Alves
# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

from random import randint
from os import system

pergunta = '[Enter] Continuar jogando\n[0] Sair do jogo\nOpção: '

print('Jogo de Craps')
while True:
    input('[Enter] Jogar dados ')
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    total = dado1+dado2
    print('Dado 1: {}'.format(dado1))
    print('Dado 2: {}'.format(dado2))
    print('Total: {}'.format(total))
    if total in (7, 11):
        print('Natural!! Você ganhou!')
        input('[Enter] Ok ')
    elif total in (2, 3, 12):
        print('Craps!! Você perdeu!')
        input('[Enter] Ok ')
    else:
        print('Ponto!! Jogue os dados até tirar [{}] novamente!'.format(total))
        input('[Enter] Ok ')
        system('clear')
        ponto = total
        while True:
            print('Ponto: {}'.format(ponto))
            input('[Enter] Jogar dados ')
            dado1 = randint(1, 6)
            dado2 = randint(1, 6)
            total = dado1+dado2
            print('Dado 1: {}'.format(dado1))
            print('Dado 2: {}'.format(dado2))
            print('Total: {}'.format(total))
            if total == ponto:
                print('Você venceu!!')
                input('[Enter] Ok ')
                break
            if total == 7:
                print('Você perdeu!!')
                input('[Enter] Ok ')
                break
            input('[Enter] Ok ')
            system('clear')

    resposta = input(pergunta)
    if resposta == '0':
        break

    system('clear')