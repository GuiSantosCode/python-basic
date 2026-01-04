print('🛡️ O GPS do Explorador (Foco: Tuplas)')

def gerar_coordenadas(a, b):
    ponto_destino = (a , b,)
    return ponto_destino

a_input = input('Digite um valor: ')
b_input = input('Digite outro valor: ')

print(gerar_coordenadas(a_input, b_input))