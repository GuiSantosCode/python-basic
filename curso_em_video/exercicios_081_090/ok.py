print('--- Lista composta: Boletim ---')

# Preenchimento
lista = []
dado_temporario = []

qntd_aluno = int(input('Quantos alunos você quer cadastrar? '))

for i in range(qntd_aluno):
    nome = input(f'Nome do {i+1}º aluno: ')
    dado_temporario.append(nome)
    
    for n in range(2):
        nota = float(input(f'Digite a {n+1}ª nota: '))
        dado_temporario.append(nota)
    
    # Cálculo da média inserido logo no cadastro para otimizar
    media = (dado_temporario[1] + dado_temporario[2]) / 2
    dado_temporario.append(media)
    
    lista.append(dado_temporario[:])
    dado_temporario.clear()

# Exibição do Menu
print("""
0 - Ver Boletim Completo
-----------------------""")
for pos, aluno in enumerate(lista, start=1):
    print(f'{pos} - {aluno[0]}')

escolha = int(input('\nDe quem você quer ver as notas? '))

if escolha == 0:
    # Uso de aspas triplas para o cabeçalho da tabela
    print(f"""
=========================================================
NOME          NOTA(1)      NOTA(2)      MÉDIA        
=========================================================""")
    for aluno in lista:
        print(f'{aluno[0]:<13}{aluno[1]:<13.1f}{aluno[2]:<13.1f}{aluno[3]:.1f}')
    print("=========================================================")

elif 1 <= escolha <= len(lista):
    # Acesso direto pelo índice (escolha - 1)
    aluno = lista[escolha - 1]
    print(f'\nAs notas de {aluno[0]} são: {aluno[1]} e {aluno[2]}')

else:
    print('Opção inválida!')

print(f'\nDados brutos da lista: {lista}')