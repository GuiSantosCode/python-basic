print('------ Resultado das provas! ------')

lista_nota = []

while True:
    add_lista = float(input('Digite uma nota: '))
    lista_nota.append(add_lista)
    continuar = input('APERTE ENTER PARA CONTINUAR: ') #flag
    if not continuar == '':
        break

nota_total = 0
qntd_nota = 0

for nota in lista_nota:
    nota_total += nota
    qntd_nota += 1

media = nota_total / qntd_nota

print(f'{media:.2f}')

if media < 5:
    print('REPROVADO!')
elif media <= 6.9:
    print('RECUPERAÇÃO!')
else: 
    print('APROVADO!')