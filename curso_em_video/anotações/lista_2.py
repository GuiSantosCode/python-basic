# =================================================================
# CURSO EM VÍDEO - PYTHON MUNDO 3
# Aula 18: Listas (Parte 2) - Listas Compostas
# =================================================================

# 1. CONCEITO BÁSICO
# Listas compostas ocorrem quando colocamos uma lista dentro de outra.
# É a base para estruturas como matrizes e tabelas de dados.
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # IMPORTANTE: Use [:] para criar uma cópia e não uma ligação

# 2. DECLARAÇÃO DIRETA
# Podemos definir os dados aninhados logo na atribuição.
povo = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

# 3. ACESSANDO DADOS
# O primeiro colchete acessa a lista interna, o segundo acessa o item dentro dela.
print(povo[0])       # ['João', 19]
print(povo[0][0])    # João
print(povo[2][1])    # 13 (Idade de Joaquim)

# 4. ITERAÇÃO (FOR)
# Podemos varrer a lista e desempacotar ou acessar os índices internos.
for p in povo:
    print(f'{p[0]} tem {p[1]} anos de idade.')

# 5. ESTRUTURA DE LEITURA (INPUT)
galera_nova = list()
dado = list() # Lista auxiliar/temporária

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera_nova.append(dado[:]) # Faz a cópia dos dados atuais
    dado.clear() # Limpa a lista auxiliar para a próxima repetição

# 6. RESUMO TÉCNICO
# .append() -> Adiciona a sublista
# .clear()  -> Limpa a lista temporária
# [:]       -> Fatiamento total que gera a cópia física dos dados

# =================================================================
# TROFÉUS DA AULA (Exercícios para praticar)
# Faça Agora: 084, 085, 086
# Deixe para a Segunda Run (Complexidade maior): 087, 088, 089
# =================================================================