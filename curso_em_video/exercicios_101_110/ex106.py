print('--- Função 3: Utilizando help e cores ---')

from rich import print
# FUNÇÃO
def sos(c): # c == comando
    help(c)  
    
# PROGRAMA PRINCIPAL
comando = ''
while True:
    comando = str(input('Importar função: '))
    if comando.upper() == 'FIM':
        break
    else:
        print(f'[red]---- BIBLIOTECA {comando.upper()} ----[/red]')
        sos(comando)