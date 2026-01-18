#Uso de ferramentas
from numeros import ler_numeros, analisar_numeros

def main():
    numeros_positivos = ler_numeros()
    resultado = analisar_numeros(numeros_positivos)

    if resultado:
        print('Comprimento, soma e maior número: ')
        print(resultado)
    else: 
        print('Nenhum número positivo foi digitado!')

if __name__ == '__main__': #Botão ligar
    main()