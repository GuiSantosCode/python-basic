print('------- Analisar notas ------')

def analisar_notas(notas):
    media_notas = sum(notas) / len(notas)
    
    relatorio = {'maior nota': max(notas),
                 'menor nota': min(notas),
                 'media nota': media_notas,
                 'situacao': 'APROVADO' if media_notas >= 7 else 'REPROVADO'}
    return relatorio
minhas_notas = [10, 8.5, 7.0, 6.5, 5.0]

print(analisar_notas(minhas_notas))