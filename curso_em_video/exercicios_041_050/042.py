print('------ Equilátero, isósceles ou escaleno! ------')

def triangulo(lado_1, lado_2, lado_3):
    if lado_1 == lado_2 and lado_1 == lado_2:
        return 'Equilátero!'
    elif lado_1 == lado_2 or lado_1 == lado_3:
        return 'Isósceles!'
    else: 
        return 'Escaleno!'

a = int(input('Digite o valor do lado A: '))
b = int(input('Digite o valor do lado B: '))
c = int(input('Digite o valor do lado C: '))

print(triangulo(a, b, c))