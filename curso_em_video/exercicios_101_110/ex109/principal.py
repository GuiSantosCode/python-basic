import time
import relatorio

# Perguntas
perguntas = [
    {'Qual o sobrenome do casal de irmãos Chris e Claire: ':'redfield'},
    {'Em que resident evil morreu o vilão mais icônico da franquia (ex: 7): ':'5'},
    {'Qual nome da pistola que o Leon usou no último jogo em que apareceu? ':'requiem'},
    {'Qual nome do inimigo comum em resident evil que é cego? ':'licker'},
    {'Qual novo personagem foi incluído no novo jogo de resident evil? ':'grace'}
]

# PROGRAMA PRINCIPAL

print('--- QUIZ DE RESIDENT EVIL ---')

print('5 perguntas começando a seguir', end='')
for i in range(3):
    print('.', end='', flush=True)
    time.sleep(0.50)
print('\n')
    
acertos = 0
erros = 0

for pos, item in enumerate(perguntas,start=1):
    for k, v in item.items():
        print(f'{pos} - {k}')
        resposta = str(input('Resposta: ')).lower().strip()
        if resposta == v:
            print('Correto!')
            acertos += 1
        else: 
            print(f'Errado, a resposta correta seria: {v}')
            erros += 1

taxa = (relatorio.acertos(acertos, erros))
print(f'A taxa de acerto foi: {taxa}%')

jogo = (relatorio.jogo(acertos))
print(f'\nO jogo que você ganhou foi: ')
time.sleep(2)
print(f'------- {jogo} --------')