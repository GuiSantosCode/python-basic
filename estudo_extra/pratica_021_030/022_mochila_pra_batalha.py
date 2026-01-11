print('--- Mochila pra batalha ---')

obrigatorios = ['Lanterna', 'Walkie_talkie', 'Taco de beisebol', 'Molotov']

mochila = [] 

print('Digite sair quando terminar!')

while True:
    novo_item = input('Qual item você quer adicionar a mochila? ')
    
    if novo_item.lower() == 'sair':
        break
    elif novo_item in obrigatorios:
        mochila.append(novo_item)
        print(f'Dusty adicionou {novo_item} a mochila!')
    else: 
        print('Nancy - Isso é inútil agora, pegue outra coisa!')
    
print(f'Bora, na mochila tem {mochila}')