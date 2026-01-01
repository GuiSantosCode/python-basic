print('------ O Grupo de RPG (HellFire) ------')
print('Dustin vai conferir a lista de presença')

lista_de_membros = ['Mike', 'Dustin', 'Lucas', 'Will']

novo_membro = input('Digite seu nome: ')

if novo_membro in lista_de_membros:
    print(f'{novo_membro} já faz parte do grupo!')
else:
    print(f'{novo_membro}, Bem vindo(a) ao Hellfire!')
    lista_de_membros.append(novo_membro)


