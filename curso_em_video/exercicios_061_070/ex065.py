print('------ Flag ------')

continuar = 's'
numero = 0
soma_numeros = 0
qntd_numeros = 0

while continuar == 's':
    numero = int(input('Digite um número: '))
    if qntd_numeros == 0:
        menor_numero = numero
        maior_numero = numero
        
    if numero > maior_numero:
        maior_numero = numero
        
    if numero < menor_numero:
        menor_numero = numero
        
    soma_numeros += numero
    qntd_numeros += 1
    continuar = input('Quer continuar? s/n: ').lower()
    
media_numeros = soma_numeros / qntd_numeros
    
print(f'Média = {media_numeros}')
print(f'Menor número = {menor_numero}')
print(f'Maior número = {maior_numero}')