#Caixa de ferramentas
def ler_numeros():
    numeros_positivos = []

    while True:
        num = int(input('Digite um número: '))
        if num == 0:
            break
        if num > 0:
            numeros_positivos.append(num)

    return numeros_positivos


def analisar_numeros(lista):
    if not lista:
        return None
    
    return len(lista), sum(lista), max(lista)
        
def main():
    numeros_positivos = ler_numeros()
    resultado = analisar_numeros(numeros_positivos)

    if resultado:
        print('Comprimento, soma e maior número: ')
        print(resultado)
    else: 
        print('Nenhum número positivo foi digitado!')