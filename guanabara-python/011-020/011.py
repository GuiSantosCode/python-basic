print('------ Quantidade de tinta por demão ------\n')

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
demao = float(input('Quantas demãos você vai dar? '))
area = largura * altura 
qntd_tinta = (area / 2) * demao

print(f'\nSua parede tem {area} m²!')
print(f'Você precisa de {qntd_tinta} litros de tinta! Para {demao:.0f} demão de tinta!')