# =================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# Aula 22: Módulos e Pacotes
# =================================================================

# 1. CONCEITO DE MODULARIZAÇÃO
# Surgiu na década de 60 para dividir programas grandes em partes.
# Foco em aumentar a legibilidade e facilitar a manutenção.

# 2. CRIANDO MÓDULOS
# Basta criar um arquivo .py separado com as suas funções.
# No arquivo principal, você usa o comando 'import'.

def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f

def dobro(n):
    return n * 2


# 3. IMPORTANDO (import vs from)
# import uteis -> Importa o módulo inteiro.
# from uteis import dobro -> Importa apenas a função específica.

import uteis
print(uteis.dobro(5))


# 4. PACOTES (BIBLIOTECAS)
# São pastas que agrupam módulos por categorias ou assuntos.
# Útil quando o projeto cresce demais para um único módulo.
# Deve-se criar um arquivo __init__.py dentro de cada pasta.

# Estrutura de exemplo:
# - projeto/
#   - main.py
#   - utilidades/
#       - __init__.py
#       - moedas/
#           - __init__.py
#       - dados/
#           - __init__.py


# 5. VANTAGENS
# Organização do código: O programa principal fica muito menor.
# Reutilização: Você pode levar seus módulos para outros projetos.
# Facilidade de manutenção: Fica mais fácil achar e corrigir erros.


# =================================================================
# TROFÉUS DA AULA (Exercícios para praticar)
# Faça Agora: (crie seus próprios módulos com funções simples)
# Deixe para a Segunda Run: (organizar em pacotes com subpastas)
# =================================================================
