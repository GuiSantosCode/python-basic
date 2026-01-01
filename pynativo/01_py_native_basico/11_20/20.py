print('Exercício 20: Imprimir Padrão Numérico Inverso')

#Loop externo que define o número(i) a ser exibido
for i in range(1, 5 + 1):
    #Loop interno que define quantas vezes o número(i) aparecerá na linha
    for j in range(5 - i + 1):
        print(i, end=" ")
    print()