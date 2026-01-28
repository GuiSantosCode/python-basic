# =================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# Aula 21: Funções (Parte 2)
# =================================================================

# 1. INTERACTIVE HELP
# Use help() no console ou no código para ver a documentação de comandos.
# help(print)

# 2. DOCSTRINGS
# É a documentação da sua própria função, escrita entre aspas triplas.
def somar(a, b, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor (opcional)
    """
    s = a + b + c
    print(f'A soma vale {s}')

# 3. PARÂMETROS OPCIONAIS
# Definir c=0 permite que a função funcione mesmo sem o terceiro valor.
somar(3, 2) 

# 4. ESCOPO DE VARIÁVEIS
# Variável Global: existe no programa inteiro.
# Variável Local: existe apenas dentro da função.
def teste():
    global n1 # Faz o Python usar o n1 global em vez de criar um local
    n1 = 5 
    print(f'N1 local vale {n1}')

n1 = 2
teste()
print(f'N1 global vale {n1}')

# 5. RETORNO DE VALORES (return)
# Permite que a função devolva um resultado para ser guardado em variável.
def somar_retorno(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar_retorno(3, 2, 5)
r2 = somar_retorno(2, 2)
print(f'Os resultados foram {r1} e {r2}')

# =================================================================
# TROFÉUS DA AULA (Exercícios para praticar)
# Faça Agora: 101, 102, 103, 104
# Deixe para a Segunda Run: 105, 106
# =================================================================