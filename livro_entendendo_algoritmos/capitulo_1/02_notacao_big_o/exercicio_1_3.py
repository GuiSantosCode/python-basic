print('''
EXERCÍCIO: 1.3
Você tem um nome e deseja encontrar o número de telefone para esse nome em uma agenda telefônica.
Resposta: O(log n)    
''')

def encontrar_telefone(agenda, alvo):
    baixo = 0 # Menor índice da lista
    alto = len(agenda) - 1 # Maior índice da lista
    
    while baixo <= alto: # Não tem sentido o alto ser menor que o baixo
        meio = baixo + alto // 2 
        chute_nome = agenda[meio]['nome'] # Acessamos o indice do meio da agenda, e pegamos o nome.
        
        if chute_nome == alvo:
            return print(f'O número de {alvo} é: {agenda[meio]['tel']}')
        
        if chute_nome > alvo:
            alto = meio - 1
        else:
            baixo = meio + 1
            
    return 'Nome não encontrado!'

agenda_ordenada = [
    {'nome': 'Ana', 'tel': '99183-9042'},
    {'nome': 'Beatriz', 'tel': '99962-6991'},
    {'nome': 'Guilherme', 'tel': '98806-8723'},
    {'nome': 'Suarez', 'tel': '99876-3452'},
    {'nome': 'Zoraide', 'tel': '98876-4590'}
]

alvo_input = (input('De qual nome você quer o número? '))

encontrar_telefone(agenda_ordenada, alvo_input)