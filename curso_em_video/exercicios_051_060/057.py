print('------ Digite seu sexo ------')

sexo = ''
while sexo not in ['m', 'f']:
    sexo = str(input('Qual o seu sexo M/F: ')).lower().strip()
    if sexo not in ['m', 'f']:
        print(f'"{sexo}" não é aceito, digite m ou f!')
        
print('Obrigado pela informação!')