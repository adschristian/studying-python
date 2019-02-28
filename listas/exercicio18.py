# author: Christian Alves
import os
'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação Python. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada.
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
a. O total de votos computados;
b. Os númeos e respectivos votos de todos os jogadores que receberam votos;
c. O percentual de votos de cada um destes jogadores;
d. O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado
aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá
executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois
parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e
retornará o valor calculado. Os dados são fictícios e podem mudar a cada execução do
programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um
arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
'''
import os
from datetime import datetime

jogadores = dict()

print('Enquete: Quem foi o melhor jogador?\n')
while True:
    print('Pressione [0] para sair')
    voto = int(input('Número do jogador: '))
    if voto == 0:
        break

    if voto not in range(1, 24):
        print('Informe um valor entre 1 e 23 ou 0 [zero] para sair!')
        continue

    if jogadores.get(voto):
        jogadores[voto] += 1
    else:
        jogadores[voto] = 1

os.system('clear')

texto = ''
texto += 'Resultado da votação' + 2*'\n'
votos = sum(jogadores.values())

texto += 'Foram computados {} votos.'.format(votos) + 2*'\n'

for num, qtd in jogadores.items():
    porcentagem = qtd*100/votos
    texto += 'Jogador {:>2} {:>10} votos {:10}%\n'.format(num, qtd, round(porcentagem, 1))

melhor = max(jogadores, key=jogadores.get)
qtd = jogadores[melhor]
porcentagem = qtd*100/votos
texto += 'O melhor jogador foi o número {}, com {} votos, correspondendo a {}% do total'.format(melhor, qtd, round(porcentagem, 1))
print(texto)

texto += 3*'\n'

arquivo = open('arquivos/e18-relatorio.txt', 'a')
arquivo.write(str(datetime.utcnow())+'\n')
arquivo.write(texto)
arquivo.close()