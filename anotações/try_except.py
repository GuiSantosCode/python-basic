# ==========================================================
# ANOTAÇÕES: TRATAMENTO DE ERROS E EXCEÇÕES (TRY... EXCEPT)
# Referência: Curso Python #23 - Gustavo Guanabara
# ==========================================================

"""
DIFERENÇA ENTRE ERRO DE SINTAXE E EXCEÇÃO:
- Erro de Sintaxe: Escrita incorreta do código (ex: 'primt' em vez de 'print').
- Exceção: O código está escrito corretamente, mas ocorre um erro durante a 
  execução (ex: divisão por zero, variável não definida, tipo de dado errado).

ESTRUTURA COMPLETA:
try:
    # Operação que pode gerar problemas
except:
    # O que fazer caso ocorra uma falha
else:
    # O que acontece se o 'try' der certo (opcional)
finally:
    # O que acontece independente de erro ou sucesso (opcional)
"""

# 
# --- EXEMPLO PRÁTICO ---

try:
    # Entrada de dados
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    # Tratando erros de tipos ou valores digitados
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    # Tratando erro específico de divisão por zero
    print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
    # Tratando caso o usuário interrompa a execução (ex: Ctrl+C)
    print('\nO usuário preferiu não informar os dados.')

except Exception as erro:
    # Tratamento genérico para identificar outros erros
    print(f'O erro encontrado foi: {erro.__cause__}')

else:
    # Executado apenas se não houver exceção
    print(f'O resultado é {r:.2f}')

finally:
    # Sempre executado ao final (útil para fechar conexões ou arquivos)
    print('Volte sempre! Muito obrigado.')


# --- PRINCIPAIS EXCEÇÕES CITADAS ---
# NameError: Variável não definida.
# ValueError: Valor inválido (ex: letra onde se espera número).
# ZeroDivisionError: Divisão por zero.
# TypeError: Operação entre tipos incompatíveis (ex: dividir string por int).
# IndexError: Índice de lista inexistente.
# KeyError: Chave de dicionário inexistente.
# ModuleNotFoundError: Módulo/Biblioteca não encontrada no import.