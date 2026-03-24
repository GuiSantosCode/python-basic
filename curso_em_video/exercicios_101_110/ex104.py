print('--- Função 2: Validação de números inteiros ---')

def leiaint():
    while True:
        numero = input('Digite um número: ')
        if numero.isnumeric():
            print(f'O número digitado foi: {numero}')
            break

leiaint()