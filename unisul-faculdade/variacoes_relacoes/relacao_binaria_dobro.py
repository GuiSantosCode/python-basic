print('')

# Números inteiros de 1 a 5
dominio = [1, 2, 3, 4, 5]
# O resultado do dobro de cada número do domínio
contradominio = []
# Relação entre domínio e contradomínio 'lista de pares ordenados'
relacao = []


# Adicionando os números a 'contradominio'
for a in dominio:
    b = a * 2
    contradominio.append(b)

# Criando a lista de relação entre o domínio e o contradomínio
for c in dominio:
    par = (dominio[c - 1], contradominio[c - 1])
    relacao.append(par)
# relacao = list(zip(dominio, contradominio)) == substitui todo o loop acima

print(f'Domínio = {dominio}')
print(f'Contradomínio = {contradominio}')
print(f'Relação = {relacao}')