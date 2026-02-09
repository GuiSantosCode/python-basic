print('--- Função: Área do terreno ---')

def area(l, c):
    print(f'A área do terreno é: {l * c}')

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

area(largura, comprimento)