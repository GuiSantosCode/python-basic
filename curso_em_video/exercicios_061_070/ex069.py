print('------ Dados das pessoas ------')

maior_de_idade = 0
qntd_homem = 0
qntd_mulher_jovem = 0

while True: 
    print('-'*50)
    sexo = input('Você é do sexo masculino ou feminino? m/f: ').lower()
    idade = int(input('Digite sua idade: '))
    
    if idade >= 18:
        maior_de_idade += 1
    if sexo == 'm':
        qntd_homem += 1
    if sexo == 'f' and idade < 20:
        qntd_mulher_jovem += 1
    
    continuar = input('Quer continuar? s/n: ').lower()
    if not continuar == 's':
        break

print(f'\nPessoas maiores de idade: {maior_de_idade}')
print(f'Quantidade de homem: {qntd_homem}')
print(f'Mulheres com menos de 20 anos: {qntd_mulher_jovem}')