print('--- Listas: enumerate, cores ---')

from rich import print

print('')

lista = []

for i in range(5):
    valor = float(input('Digite um valor: '))
    lista.append(valor)

lista.sort()

for pos, item in enumerate(lista, start=1):
    if pos == 1:
        print(f'[red] {pos}° - {item} [/red]', 'Menor valor!')
    elif pos == 5:
        print(f'[green] {pos}° - {item} [/green]', 'Maior valor!')
    else:
        print(f'{pos}° - {item}')