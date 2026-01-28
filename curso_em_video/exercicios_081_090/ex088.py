from random import randint 

print('--- Mega Sena ---')
jogos = []
dado_temporario = []

qntd_jogos = int(input('Quantos jogos você quer fazer? '))

for i in range(qntd_jogos):
    for j in range(6):
        while True:
            numero_temporario = randint(1, 60)
            if numero_temporario not in dado_temporario:
                dado_temporario.append(numero_temporario)
                break
    jogos.append(dado_temporario[:])
    dado_temporario.clear()

print(f'Esses são os seus jogos, boa sorte!')

print('-=' * 25)
for jogo in jogos:
    print(jogo)
print('-=' * 25)