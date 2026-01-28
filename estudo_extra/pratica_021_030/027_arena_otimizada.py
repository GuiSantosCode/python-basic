print('--- Cadastro de heróis ---')
guilda = []

for i in range(3):
    print(f'\nCadastro do {i+1}º Herói:')
    heroi = {
        'nome': input('Nome: '),
        'classe': input('Classe: '),
        'vida': int(input('Vida: ')),
        'ataque': int(input('Ataque: '))
    }
    guilda.append(heroi)

# Média dinâmica
media_ataque = sum(h['ataque'] for h in guilda) / len(guilda)

# Listagem usando chaves (Fica muito mais legível!)
print(f"\n{'NOME':<13} {'CLASSE':<13} {'VIDA':<13} {'ATAQUE':<13}")
for h in guilda:
    print(f"{h['nome']:<13} {h['classe']:<13} {h['vida']:<13} {h['ataque']:<13}")