print('--- Função: Contagens ---')

def contador(inicio, fim, passo):
    if inicio < fim:
        print('--- Contagem progressiva ---')
        while inicio <= fim:
            print(inicio, end=' ')
            inicio += passo
        print()
    else: 
        print('--- Contagem regressiva ---')
        while inicio >= fim:
            print(inicio, end=' ')
            inicio -= passo
        print()
        
# a)
contador(1, 10, 1)
# b)
contador(10, 0, 2)
# c)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)