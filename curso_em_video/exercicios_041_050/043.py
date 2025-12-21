print('------ Cálculo do IMC ------')

status = [
    'Abaixo do peso!',
    'Peso ideal!',
    'Sobrepeso!',
    'Obesidade!',
    'Obesidade mórbida!'
]

def imc(peso, altura):
    imc = peso / altura ** 2
    print(f'IMC: {imc:.2f}')
    
    if imc < 18.5: 
        return status[0]
    elif imc < 25:
        return status[1]
    elif imc < 30:
        return status[2]
    elif imc < 40:
        return status[3]
    else: 
        return status[4]
    
a = float(input('Digite o seu peso: '))
b = float(input('Digite sua altura: '))

print(imc(a, b))