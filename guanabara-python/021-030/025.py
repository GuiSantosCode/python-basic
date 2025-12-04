print('------ Tem silva? ------')

nome = (input('Digite um nome completo: '))

if nome.find('silva') == -1:
    print(f'Não tem o nome "silva" dentro de "{nome}"')
else: 
    print(f'Tem o nome "silva" em "{nome}"')