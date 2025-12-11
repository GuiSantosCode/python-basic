#FUNÇÃO
def calcular_peso_total(itens):
    peso_acumulado = 0
    for peso in itens:
        peso_acumulado += peso
    return peso_acumulado 

#EXECUÇÃO DO PROGRAMA
print('------ Inventário de Itens Coletados ⛏️ ------')

peso_itens = [25, 8, 13, 21, 19]

peso_final = calcular_peso_total(peso_itens)

print(peso_itens)
print(peso_final)