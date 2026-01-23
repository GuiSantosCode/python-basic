print('--- Cadastro de heróis ---')

guilda = []
dados_temporarios = []

for i in range(3):
    nome = str(input('Digite o nome: '))
    classe = str(input('Digite a classe: '))
    vida = int(input('Digite a vida: '))
    ataque = int(input('Digite o ataque: '))
    
    dados_temporarios = [nome, classe, vida, ataque]
    guilda.append(dados_temporarios[:])
    dados_temporarios.clear()

# Listagem dos heróis

print(f'\n=========================================================')
print(f'NOME         CLASSE       VIDA         ATAQUE        ')
print(f'=========================================================')
for heroi in guilda:
    print(f'{heroi[0]:<13}', end='')
    print(f'{heroi[1]:<13}', end='')
    print(f'{heroi[2]:<13}', end='')
    print(f'{heroi[3]}', end='')
    print('')
print(f'=========================================================')

# Quantos personagens foram criados? 

print(f'\nPersonagens criados: {len(guilda)}')

# O personagem com maior ataque?

maior_ataque = guilda[0][3]

for heroi in guilda:
    if heroi[3] > maior_ataque:
        maior_ataque = heroi[3]
        
print(f'\nO maior ataque da guilda é: {maior_ataque}')
print(f'\nOs heróis com {maior_ataque} de ataque são: | ', end='')

for heroi in guilda:
    if heroi[3] == maior_ataque:
        print(f'{heroi[0]}', end=' | ')
    
# Personagem com menor vida? 

menor_vida = guilda[0][2]

for heroi in guilda:
    if heroi[2] < menor_vida:
        menor_vida = heroi[2]

print(f'\n\nA menor vida da guilda é: {menor_vida}')
print(f'\nOs heróis com {menor_vida} de vida são: | ', end='')

for heroi in guilda:
    if heroi[2] == menor_vida:
        print(f'{heroi[0]}',end=' | ')

# A média de ataque da equipe

media_de_ataque = sum(heroi[3] for heroi in guilda) / len(guilda)

print(f'\n\nA média de ataque da guilda é: {media_de_ataque:.2f}')
    
# =============== EXTRA ================
# Personagens com ataque acima da média
# ======================================

maior_que_70 = []
 
print(f'\nHeróis com ataque acima da média: ', end='')
for heroi in guilda:
    if heroi[3] > 70:
        maior_que_70.append(heroi[0])
print(maior_que_70)

# =============== EXTRA ================
# Personagens com vida menor que 100
# ======================================

menor_que_100 = []

print(f'\n\nHeróis com vida menor que 100: ', end='')
for heroi in guilda:
    if heroi[2] < 100:
        menor_que_100.append(heroi[0])
print(f'{menor_que_100}')