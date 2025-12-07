'''
FORMATACAO DE TEXTO
observação: frase.capitalize()
    frase = objeto
    capitalize = metodo
    () = parametro

FATIAMENTO--

frase[9:21:2]
    9 = começo
    21 = onde para
    2 = pulando de 2 em 2

frase[:5]
    inicio até o 5

frase[15:]
    15 até o final
    
frase[9::3]
    9 até o final, pulando de 3 em 3
    
    
    
ANALISE--

len(frase)
    comprimento da frase

frase.count('o')
    quantos 'o' na frase? 3
    
frase.count('o',0,13)
    quantos 'o' na frase do indice 0 ao 13? 1
    
frase.find('deo')
    procura alguma palavra na frase com 'deo'
    e mostra o indice do d, que seria o incio
    
frase.find('android')
    caso android nao esteja na frase retorna -1
    
frase.rfind('a')
    procura a posicao do 'a' de trás pra frente

'curso' in frase 
    se tiver curso na frase retorna true



TRANSFORMACAO--

frase.replace('Python','Android')
    se tiver python na frase, troca por android
    
frase.upper()
    transforma a frase toda em maiusculo
    
frase.lower()
    transforma a frase toda em minusculo

frase.capitalize()
    transforma a primeiro indice da frase em maisculo
    
frase.title()
    transforma a primeira letra de toda a palavra em maisculo

frase.strip()
    remove todos os espaços em branco do começo e do final da frase
    
frase.rstrip()
    o r antes do strip significa direita
    remove todos os espaços em branco do final da frase
        
frase.lstrip()
    o l antes do strip significa esquerda
    remove todos os espaços em branco do inicio da frase
    


DIVISAO--
 
frase.split()
    cria um indexador(indice) pra cada palavra da frase
    usar [-1], [-2]... conta de trás pra frente
    
    
    
JUNCAO--

'-'.join(frase)
    adiciona - entre as palavras
'''