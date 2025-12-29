print('Exercício 6: Escreva todo o conteúdo de um arquivo em um novo arquivo, pulando a linha 5.')

# Abre o arquivo "teste.txt" em modo de leitura ("r" de read)
with open("teste.txt", "r") as arquivo_origem:
    # Lê todas as linhas do arquivo e as armazena em uma lista chamada 'linhas'
    linhas = arquivo_origem.readlines()

# Abre (ou cria) um novo arquivo chamado "novo_arquivo.txt" em modo de escrita ("w" de write)
with open("novo_arquivo.txt", "w") as arquivo_destino:
    contador = 0
    
    # Itera sobre cada linha que foi lida do arquivo original
    for linha in linhas:
        # Verifica se estamos na 5ª linha (índice 4, pois a contagem começa em 0)
        if contador == 4:
            # Incrementa o contador e pula para a próxima iteração (ignora esta linha)
            contador += 1
            continue
        else:
            # Escreve a linha atual no novo arquivo
            arquivo_destino.write(linha)
        
        # Incrementa o contador a cada linha processada
        contador += 1