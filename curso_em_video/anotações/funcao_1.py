# =================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# Aula 20: Funções (Parte 1)
# =================================================================

# 1. CONCEITO BÁSICO
# Funções (rotinas) servem para automatizar tarefas repetitivas.
# São definidas pela palavra-chave 'def'.
def linha():
    print('-' * 30)

linha()
print('    CURSO EM VÍDEO    ')
linha()

# 2. FUNÇÕES COM PARÂMETROS
# Podemos passar informações para dentro da função.
def mensagem(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

mensagem('SISTEMA DE ALUNOS')

# 3. PRÁTICA: SOMA COM PARÂMETROS
def soma(a, b):
    s = a + b
    print(f'A soma A + B = {s}')

soma(4, 5)
soma(a=8, b=2) # Parâmetros nomeados

# 4. EMPACOTAMENTO (*args)
# Quando não sabemos quantos valores serão passados.
# O Python cria uma TUPLA com os valores.
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

contador(2, 1, 7)
contador(8, 0)

# 5. TRABALHANDO COM LISTAS EM FUNÇÕES
# Diferente de variáveis simples, listas passam por REFERÊNCIA.
# O que mudar na função, muda na lista original.
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1]
dobra(valores)
print(valores) # [12, 6, 18, 2]

# =================================================================
# TROFÉUS DA AULA (Exercícios para praticar)
# Faça Agora: 096, 097, 098
# Deixe para a Segunda Run: 099, 100
# =================================================================