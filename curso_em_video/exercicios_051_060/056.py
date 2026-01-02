print('------ Nome, idade e sexo ------')

idade_dos_homens = []
idade_das_mulheres = []
mulher_jovem = 0
idade_homem_velho = 0
nome_homem_velho = ''

for i in range(4):
    nome = input('Qual seu nome: ')
    sexo = input('Qual seu sexo: ')
    idade = int(input('Digite sua idade: '))
    if sexo.lower() == 'masculino':
        idade_dos_homens.append(idade)
        if idade > idade_homem_velho:
            nome_homem_velho = nome
    else: 
        idade_das_mulheres.append(idade)
        if idade < 20: 
            mulher_jovem += 1
    print('-' * 30)
    
idade_do_grupo = idade_das_mulheres + idade_dos_homens

print(f'A média de idade do grupo é: {sum(idade_do_grupo) / len(idade_do_grupo)}')
print(f'O homem mais velho é o {nome_homem_velho}, com: {max(idade_dos_homens)} anos.')
print(f'Tem {mulher_jovem} mulher(es) com menos de 20 anos!')