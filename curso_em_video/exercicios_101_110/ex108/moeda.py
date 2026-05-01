# FUNÇÕES # n = numero

def moeda(n=0, moeda='$'):
    return f'{moeda}{n:.2f}'.replace('.',',')

def aumentar(n=0, formatado = True): 
    operacao = n + 1
    return operacao if formatado is False else moeda(operacao)
    
def diminuir(n=0, formatado = True): 
    operacao = n - 1
    return operacao if formatado is False else moeda(operacao)

def dobro(n=0, formatado = True):
    operacao = n * 2
    return operacao if formatado is False else moeda(operacao)

def metade(n, formatado = True):
    operacao = n / 2
    return operacao if formatado is False else moeda(operacao)
