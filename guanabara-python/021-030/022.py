nome = (input('Qual seu nome completo? '))

print(f'Maiusculo:', nome.upper())
print(f'Minusculo:', nome.lower())
print(f'Comprimento inteiro:', len(nome))
print(f'Comprimento do primeiro nome:', len(nome.split()[0]))