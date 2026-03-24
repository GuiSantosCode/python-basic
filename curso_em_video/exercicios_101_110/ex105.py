print('--- Função 2: Validação de números inteiros ---')

def notas():
    notas = []
    qntd_alunos = int(input('Quantos alunos você quer adicionar? '))
    for i in range(qntd_alunos):
        nota = float(input('Digite sua nota: '))
        notas.append(nota)        
    informacoes = {'alunos': len(notas),
                   'maior nota': max(notas),
                   'menor nota': min(notas),
                   'media': sum(notas) / len(notas)}
    if informacoes['media'] >= 7:
        return informacoes, 'Turma aprovada!'
    else: 
        return informacoes, 'turma reprovada!'                    
print(notas())