print('--- Lista composta: Boletim ---')

# Preenchimento

lista = []
dado_temporario = []

qntd_aluno = int(input('Quantos alunos você quer cadastrar? '))

for i in range(qntd_aluno):
    nome = input('Digite seu nome: ')
    dado_temporario.append(nome)
    for i in range(2):
        nota = float(input('Digite sua nota: '))
        dado_temporario.append(nota)
    lista.append(dado_temporario[:])
    dado_temporario.clear()

for aluno in lista:
    media = (aluno[1] + aluno[2]) / 2
    aluno.append(media)

# Exibição 

print('\n0 - Boletim')
for pos, aluno in enumerate(lista, start=1):
    print(f'{pos} - {aluno[0]}')

escolha = int(input('De quem você quer ver as notas? '))
if escolha == 0:
    print(f'\n=========================================================')
    print(f'NOME         NOTA(1)      NOTA(2)      MÉDIA        ')
    print(f'=========================================================')
    for aluno in lista:
        print(f'{aluno[0]:<13}', end='')
        print(f'{aluno[1]:<13.2f}', end='')
        print(f'{aluno[2]:<13.2f}', end='')
        print(f'{aluno[3]}', end='')
        print('')
    print(f'=========================================================')
else:
    print()
    for pos, aluno in enumerate(lista, start=1):
        if escolha == pos:
            print(f'As notas de {aluno[0]} são: {aluno[1]} | {aluno[2]}')
            
print(lista)