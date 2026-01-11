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
        # Calcula o índice central entre os limites atuais
        meio = (baixo + alto) // 2
        chute = lista[meio]

        # Caso 1: Item encontrado
        if chute == item:
            return meio
        
        # Caso 2: O chute foi alto demais, ajusta o limite superior
        if chute > item:
            alto = meio - 1
        
        # Caso 3: O chute foi baixo demais, ajusta o limite inferior
        else:
            baixo = meio + 1
            
    return None

# --- Preparação dos dados ---
minha_lista = [9, 7, 5, 3, 1]
minha_lista.sort()  # A lista DEVE estar ordenada para a busca binária funcionar

# --- Testes ---
print(f"Índice do elemento 3: {pesquisa_binaria(minha_lista, 3)}")
print(f"Resultado para item inexistente (-1): {pesquisa_binaria(minha_lista, -1)}")