print('------ Tem santo no começo? ------')

cidade = (input('Digite o nome de uma cidade? '))

if ('santo' in cidade.split()[0]) == True:
    print(f'"{cidade}" começa com "santo"')
else:
    print(f'Não tem "santo" no começo de "{cidade}"')