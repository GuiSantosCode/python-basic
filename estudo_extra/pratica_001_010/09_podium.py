print('------ Desafio de meste: Podium ------')

competidores = [{'nome': 'Mariana', 'pontos': 90},
                {'nome': 'Guilherme', 'pontos': 85},
                {'nome': 'Gustavo', 'pontos': 40},
                {'nome':'Ruan', 'pontos': 50},
                {'nome':'Josué', 'pontos': 70}]

premios = ('Ouro', 'Prata', 'Bronze')

def premiar_jogadores(lista):
    lista.sort(key=lambda x: x['pontos'], reverse=True)

    for i in range(3):
        ganhador = lista[i]['nome']
        medalha = premios[i]
        pontuacao = lista[i]['pontos']
        print(f'{i+1}º lugar: {ganhador} - Medalha: {medalha} - Pontuação: {pontuacao} ')

premiar_jogadores(competidores)