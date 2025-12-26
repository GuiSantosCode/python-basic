print('------ Soma de 6 números (Resolução 2) ------')

num_par = []

for i in range(6):
    valores = int(input('DIgite um valor: '))
    if valores % 2 == 0:
        num_par.append(valores)

num_par.sort()

print(f'A lista dos pares em ordem ficaria:', num_par)
print('O menor da lista é o :', min(num_par))
print('O maior é:', max(num_par))
print(sum(num_par ))
        
    
    
    