# author: Christian Alves
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('Nome de usuário: ')
senha = input('Senha: ')

while senha == nome:
    print('Erro\nSenha não pode ser igual ao nome de usuário.')
    senha = input('Senha: ')