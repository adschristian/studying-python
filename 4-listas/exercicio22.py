# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# necessita da esfera;
# necessita de limpeza;
# necessita troca do cabo ou conector;
# quebrado ou inutilizado
# Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir um relatório.

from os import system

situacao = []

while True:
    opcao = input('1) Necessita da esfera\n2) Necessita de limpeza\n3) Necessita troca do cabo ou conector\n4) Quebrado ou inutilizável\n0) Encerrar\nOpção: ')
    if opcao == '0':
        break
    
    if opcao in ('1','2','3','4'):
        situacao.append(opcao)
    else:
        print('Opção inválida!')
    
    system('clear')

system('clear')
print('Relatório\n')

total = len(situacao)
esfera = situacao.count('1')
limpeza = situacao.count('2')
troca = situacao.count('3')
quebrado = situacao.count('4')
print('Quantidade de mouses: {}'.format(total))
print('Necessita da esfera: {} mouses ({}%)'.format(esfera, round(esfera*100/total)))
print('Necessita de limpeza: {} mouses ({}%)'.format(limpeza, round(limpeza*100/total)))
print('Necessita troca do cabo ou conector: {} mouses ({}%)'.format(troca, round(troca*100/total)))
print('Quebrado/Inutilizável: {} mouses ({}%)'.format(quebrado, round(quebrado*100/total)))