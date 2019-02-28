# author: Christian Alves
# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Sexo (m/f): ').lower()

if sexo == 'm': print('Masculino')
elif sexo == 'f': print('Feminino')
else: print('Sexo inválido')