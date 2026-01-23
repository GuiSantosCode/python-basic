print('--- Software da turma ---')

turma = []
dado_temporario = []

for i in range(5):
    nome = str(input('Digite seu nome: '))
    nota = float(input('Digite sua nota: '))    
    dado_temporario = [nome, nota]
    turma.append(dado_temporario[:])
    dado_temporario.clear()
    
print(f'Os alunos da turma são: {turma}')

# A)
print('\nA)', end=' ')
print(f'Quantos alunos cadastrados: {len(turma)}')

# B)
print('\nB)', end=' ')
notas = []
for aluno in turma:
    notas.append(aluno[1])
print(f'A média da turma: {sum(notas) / len(notas)}')

# C)
print('\nC)', end=' ')
maior_nota = turma[0][1]
for aluno in turma: 
    if aluno[1] > maior_nota:
        maior_nota = aluno[1]
print(f'A maior nota foi: {maior_nota}')

print(f'Os alunos que atingiram essa nota foram: ')
for aluno in turma:
    if aluno[1] == maior_nota:
        print(f'Aluno: {aluno[0]} | Nota: {aluno[1]}')
        
# D)
print('\nD)', end=' ')
menor_nota = turma[0][1]
for aluno in turma:
    if aluno[1] < menor_nota:
        menor_nota = aluno[1]
print(f'A menor nota foi: {menor_nota}')

print(f'Os alunos que atingiram essa nota foram: ')
for aluno in turma:
    if aluno[1] == menor_nota:
        print(f'Aluno: {aluno[0]} | Nota: {aluno[1]}')    