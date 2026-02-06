'''
Conta de trás pra frente: 
    for c in range(6, 0, -1):
        print(c)
    print('FIM')
    
Conta pulando: 
    for c in range(0, 7, 2):
        print(c)
    print('FIM')
    
Uso de váriavel pra controle do for:
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))

    for c in range(i, f, p):
        print(c)
        
Dado e posição:
Da o índice e o valor de dentro da lista.
Se colocar ao lado de lanche start=1, ele começa a dar os índices a apartir de 1.
Exemplo:
    for pos, comida in enumerate(lanche, start=1):
        print(f'Eu vou comer{comida} na posição {pos}')
'''