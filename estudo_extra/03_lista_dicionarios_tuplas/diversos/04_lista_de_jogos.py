print('\n------ Lista de Jogos 🎮 ------\n')

lista_de_jogos = [
    {'Jogo': 'Horizon Zero Dawn',
     'Gênero': 'Ação e Aventura',
     'Nota': 8.0},
    
    {'Jogo': 'Resident Evil 4',
     'Gênero': 'Survivor Horror e Ação',
     'Nota': 9.5},
    
    {'Jogo': 'Red Dead Redemption 2',
     'Gênero': 'Ação em Mundo Aberto',
     'Nota': 10.0}
    ]

soma_das_notas = 0
jogos_acima_da_media = 0

for jogos in lista_de_jogos:
    jogo = jogos['Jogo'] 
    genero = jogos['Gênero']
    nota = jogos['Nota']
    if nota >= 9.5:     
        print(f'Jogo: {jogo}  |  Gênero: {genero}  |  Nota: {nota}\n')
        soma_das_notas += nota 
        jogos_acima_da_media += 1

media_das_notas = soma_das_notas / jogos_acima_da_media
print(f'------ A média das nota dos jogos é: {media_das_notas:.2f} ------\n')