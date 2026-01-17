print('------ Cadastro de aluno -----')

def cadastrar_aluno():
    nome = input('Digite seu nome: ')
    
    nota1 = float(input('Digite sua primeira nota: '))
    while nota1 < 0 or nota1 > 10:
        print("Erro: a nota deve estar entre 0 e 10.")
        nota1 = float(input("Digite sua primeira nota: "))
    
    nota2 = float(input('Digite sua segunda nota: '))
    while nota2 < 0 or nota2 > 10:
        print("Erro: a nota deve estar entre 0 e 10.")
        nota2 = float(input("Digite sua primeira nota: "))
    
    media = (nota1 + nota2) / 2
    
    return {'nome': nome,
            'nota1': nota1,
            'nota2': nota2,
            'media': media}

lista = []

for i in range(0,3):
    lista.append(cadastrar_aluno())   
    
maior_media = float('-inf')

for item in lista:
    print(f"{item['nome']}: {item['media']}")
    if item['media'] > maior_media:
        maior_media = item['media']    
        nome_aluno = item['nome']    

print('--- MAIOR MÉDIA ---')
print(f'{nome_aluno}: {maior_media}')