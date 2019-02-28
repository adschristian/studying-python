# author: Christian Alves
# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

def lerarquivo():
    enderecos = None
    try:
        file = open('files/enderecos.txt')
        enderecos = file.readlines()
        file.close()
    except IOError:
        print('Erro de leitura.')
        exit()
    
    return enderecos

def gravararquivo(texto):
    try:
        file = open('files/relatorio.txt', 'w')
        file.write(texto)
        file.close()
    except IOError:
        print('Erro de escrita.')
        exit

def validar(endereco):
    assert isinstance(endereco, str)
    octetos = endereco.split('.')
    if len(octetos) != 4:
        return False
    
    return int(octetos[0])<256 and int(octetos[1])<256 and int(octetos[2])<256 and int(octetos[3])<256

def main():
    enderecos = lerarquivo()
    if not enderecos:
        return
    
    validos = []
    invalidos = []
    for end in enderecos:
        validos.append(end) if validar(end) else invalidos.append(end)
    
    texto = '[Endereços válidos:]\n'
    texto += ''.join(validos)
    texto += '\n'
    texto += '[Endereços inválidos:]\n'
    texto += ''.join(invalidos)
    
    gravararquivo(texto)

if __name__=='__main__':
    main()