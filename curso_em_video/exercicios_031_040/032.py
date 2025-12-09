print('------ Teste de ano BISSEXTO! ------')

ano = int(input('Digite algum ano: '))

if ano % 4 == 0:
    print(f'O ano {ano}, é bissexto!')
else: 
    print(f'O ano {ano}, não é bissexto!')