# author: Christian Alves
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Type a letter: ')
print('Vogal' if letra.lower() in ['a','e','i','o','u'] else 'Consoante')