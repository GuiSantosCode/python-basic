print('------ PROGRESSÃO ARITMÉTICA: 10 primeiros termos (Resolução 4) ------')

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
i = 0
qntd_termos = 0
mais_termos = 1

while mais_termos > 0:
    mais_termos = int(input('Quantos termos você quer adicionar? '))
    if mais_termos > 0:
        qntd_termos += mais_termos
    else:
        break
    while i < qntd_termos:
        print(termo) 
        termo += razao   
        i += 1