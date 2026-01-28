import os

tam = 55
print('=' * tam)
print(f"{'Cadastro de heróis':^{tam}}")
print('=' * tam)

# Lista final de heróis e seus atributos
guilda = []

# Quantidade de heróis que serão adicionados a guilda
qntd_heroi = int(input('Quantos heróis você quer adicionar a sua guilda? '))
os.system('cls' if os.name == 'nt' else 'clear')

# Loop que vai adicionar os heróis
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
    
# Lista dos heróis usando {} dentro de uma f string
print(f"{'Cadastro de Heróis':^{tam}}")
print(f'=' * tam)
print(f"{'NOME':<13} {'CLASSE':<13} {'VIDA':<13} {'ATAQUE':<13}")
print(f'=' * tam)

for heroi in guilda:
    print(f"{heroi['nome']:<13} {heroi['classe']:<13} {heroi['vida']:<13} {heroi['ataque']:<13}")
    
# Média dinâmica de ataque da guilda
media = sum(heroi['ataque'] for heroi in guilda) / len(guilda)

print('=' * tam)
print(f'A média de ataque da equipe é: {media}')

# Continua...