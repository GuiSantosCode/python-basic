import os
print(f'--- Dicionário: Situação de aluno ---')
aluno = {}

aluno['nome'] = str(input('Digite seu nome: '))
aluno['media'] = float(input('Digite a sua média: '))
aluno['situacao'] = ('Aprovado' if aluno['media'] >= 7 else 'Reprovado')

os.system('cls') # Limpando terminal
for key, value in aluno.items():
    print(f'{key} = {value}')