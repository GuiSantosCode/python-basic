print('Filtro de Loot Único (Foco: Conjuntos/Sets)')

bau_de_itens = ['espada', 'pocao', 'escudo', 'pocao', 'espada', 'maca']

def limpar_inventario(lista_suja):
    #set: limpa as duplicatas
    return set(lista_suja)

print(bau_de_itens)
print(limpar_inventario(bau_de_itens))