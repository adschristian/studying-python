# author: Christian Alves
# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade (Mbps): '))

tamanho_Mb = tamanho*8
tempo_segundos = tamanho_Mb/velocidade
tempo_min = tempo_segundos/60

print('Tempo de download: {} minutos'.format(round(tempo_min, 2)))