print('Lista: Verificando fechamento de "()"')

expressao = input('Digite a expressão: ')
pilha = []

for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() # Remove o último '(' pois encontrou seu par ')'
        else:
            pilha.append(')') # Adiciona um erro se fechar sem ter aberto
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')