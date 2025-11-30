import time

print('------ Lançamento de Foguete! ------')

tempo = 10
# Variável para controlar os espaços em branco (a diagonal)
indentacao = 0 
foguete = '🚀'
# Você também pode usar um desenho ASCII como '^' ou '|'

lancar = input('Aperte qualquer tecla para lançar: ')

while tempo > 0:
    # 1. Cria a linha com espaços + o foguete, simulando a diagonal
    linha_diagonal = ' ' * indentacao + f'{tempo} ' + foguete
    
    # 2. Imprime a linha
    print(linha_diagonal)
    
    # 3. Adiciona mais espaços para o próximo passo
    indentacao += 2 
    
    # 4. Diminui o tempo
    tempo -= 1
    
    # 5. Espera
    time.sleep(0.5) # Reduzi para 0.5s para ser mais rápido
    
# Depois que o loop termina
print(' ' * indentacao + 'Lançamento! 💥')