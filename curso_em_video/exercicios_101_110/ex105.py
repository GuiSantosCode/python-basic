print('--- Função 2: Validação de números inteiros ---')

# FUNÇÃO
def notas(*n, situacao=False):
    """
    Parâmetro n: Quantas notas quiser colocar dos alunos
    Parâmetro situacao: Colocar True na entrada de dados decide mostrar a situação
    Retorno: Dicionário com vários dados sobre as notas da turma
    """
    
    dados = dict()    
    dados['quantidade'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = round(sum(n) / len(n), 2)
    if situacao:
        if dados['media'] >= 7:
            dados['situacao'] = 'Passou!'
        elif dados['media'] >= 5:
            dados['situacao'] = 'Recuperação!'
        else:
            dados['situacao'] = 'Reprovou!'
    return dados
       
# ENTRADA DE DADOS  
dados = notas(9.5, 7.5, 6, situacao=True)

# SAÍDA DE DADOS
print(dados)
help(notas)