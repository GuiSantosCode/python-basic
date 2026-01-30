import os

tam = 60
print('=' * tam)
print(f"{'Cadastro de heróis':^{tam}}")
print('=' * tam)

# LISTA DE HERÓIS
guilda = []


# QUANTIDADE DE HERÓIS
qntd_heroi = int(input('Quantos heróis você quer adicionar a sua guilda? '))
os.system('cls' if os.name == 'nt' else 'clear')


# ADICIONANDO HERÓIS
for i in range(qntd_heroi):
    print(f'{i + 1}° Herói')
    print()
    heroi = {
        'nome': str(input('Nome do herói: ')),
        'classe': str(input('Classe do herói: ')),
        'vida': int(input('Vida do herói: ')),
        'ataque': int(input('Ataque do herói: ')),
    }
    guilda.append(heroi) 
    os.system('cls' if os.name =='nt' else 'clear')
    
    
# LISTAGEM DOS HERÓIS
print(f"{'Cadastro de Heróis':^{tam}}")
print(f'=' * tam)
print(f"{'NOME':<13} {'CLASSE':<13} {'VIDA':<13} {'ATAQUE':<13}")
print(f'=' * tam)

for heroi in guilda:
    print(f"{heroi['nome']:<13} {heroi['classe']:<13} {heroi['vida']:<13} {heroi['ataque']:<13}")
    print(f'=' * tam)
    
    
# MÉDIA DE ATAQUE DOS HERÓIS
media = sum(heroi['ataque'] for heroi in guilda) / len(guilda)

print('=' * tam)
print(f'A média de ataque da equipe é: {media}')
print('=' * tam)


# QUANTIDADE DE HERÓIS CRIADOS
print(f'=' * tam)
print(f'A quantidade de heróis criadas foi: {len(guilda)}')
print(f'=' * tam)



# MAIOR ATAQUE DA GUILDA
maior_ataque = max(heroi['ataque'] for heroi in guilda)
print(f'=' * tam)
print(f'O maior ataque da guilda é: {maior_ataque}')
print(f'=' * tam)


# HERÓIS COM MAIOR ATAQUE
herois_maior_ataque = [heroi['nome'] for heroi in guilda if heroi['ataque'] == maior_ataque]
print(f'=' * tam)
print(f'Os heróis com maior ataque são: {herois_maior_ataque}')
print(f'=' * tam)

# MENOR VIDA DA GUILDA
menor_vida = min(heroi['vida'] for heroi in guilda)
print(f'=' * tam)
print(f'A menor vida da guilda é: {menor_vida}')
print(f'=' * tam)

# HERÓIS COM MENOR VIDA
herois_menor_vida = [heroi['nome'] for heroi in guilda if heroi['vida'] == menor_vida]
print(f'=' * tam)
print(f'Os heróis com menor vida são: {herois_menor_vida}')
print(f'=' * tam)