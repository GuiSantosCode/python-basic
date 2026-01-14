print('------ Pesquisa Binária ------')

def pesquisa_binaria(lista, item):
    """
    Realiza uma busca binária para encontrar a posição de um item em uma lista.
    
    Args:
        lista (list): Uma lista de elementos ordenada de forma crescente.
        item: O valor que está sendo procurado na lista.
        
    Returns:
        int: O índice do item se ele for encontrado.
        None: Se o item não estiver presente na lista.
    """
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        
        meio = (baixo + alto) // 2 # Calcula o meio entre o índice mais baixo e o mais alto atuais.
        chute = lista[meio] # Armazena o item da lista que está no índice do meio.

        # Caso encontre, retorna o índice onde se encontra o número pedido.
        if chute == item:
            return meio
        
        # Se o chute for maior que o item que estamos procurando, o "novo" alto passa a ser ele, já que o chute é maior que o item.
        if chute > item:
            alto = meio - 1
        
        # Caso contrário, usamos a mesma lógica, só que com o baixo
        else:
            baixo = meio + 1
            
    return None

# --- Preparação dos dados ---
minha_lista = [2, 4, 7, 10, 15]
minha_lista.sort()  # A lista DEVE estar ordenada para a busca binária funcionar
item = int(input('Digite o item pra procurar na lista: '))

# --- Testes ---
print(f"Índice do elemento {item}: {pesquisa_binaria(minha_lista, item)}") 