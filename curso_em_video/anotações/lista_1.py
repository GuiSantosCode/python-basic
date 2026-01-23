# =================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# Aula 17: Listas (Parte 1)
# =================================================================

# 1. CONCEITO BÁSICO
# Listas são mutáveis (diferente das Tuplas).
# Podem ser declaradas com [] ou list()
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']

# 2. ADICIONANDO ELEMENTOS
lanche.append('Cookie')          # Adiciona ao final da lista
lanche.insert(0, 'Cachorro-quente') # Adiciona na posição específica, deslocando o resto

# 3. APAGANDO ELEMENTOS
del lanche[3]                    # Remove pelo índice
lanche.pop(3)                    # Remove pelo índice (geralmente usado para o último se vazio: lanche.pop())
lanche.remove('Pizza')           # Remove pelo valor (o primeiro que encontrar)

if 'Pizza' in lanche:            # Forma segura de remover sem dar erro
    lanche.remove('Pizza')

# 4. CRIANDO LISTAS COM RANGE
valores = list(range(4, 11))     # Cria lista de 4 até 10

# 5. ORDENAÇÃO
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()                   # Ordena de forma crescente
valores.sort(reverse=True)       # Ordena de forma decrescente
len(valores)                     # Tamanho da lista
valores_decrescente = sorted(valores, reverse=True) # Para guardar em uma váriavel

# 6. PRÁTICA E LAÇOS
num = [2, 5, 9, 1]
num[2] = 3 # Alterando valor (Listas são mutáveis)

for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}!')

# 7. PECULIARIDADE DO PYTHON: LIGAÇÃO VS CÓPIA
a = [2, 3, 4, 7]
b = a         # Cria uma LIGAÇÃO (O que mudar em 'b' muda em 'a')
b = a[:]      # Cria uma CÓPIA (O que mudar em 'b' NÃO afeta 'a')

# =================================================================
# TROFÉUS DA AULA (Exercícios para praticar)
# Faça Agora: 078, 079, 081
# Deixe para a Segunda Run (Desafios lógicos): 080, 082, 083
# =================================================================