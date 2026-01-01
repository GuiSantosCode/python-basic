print('Exercício 19: Imprima os números primos alternados até 20.')

def is_primo(num):
    #Se for menor que 2 não pode ser primo, portando retorna falso imediatamente
    if num < 2: 
        return False 
    #Se tiver um divisor maior que a raiz quadrada, também terá um menor que ela.
    #Então iteramos um índice apenas até a raiz quadrada. O '+ 1' é pra tratar o índice
    #Se tiver um divisor além dele mesmo e 1, retorna falso. Senao retorna verdadeiro. 
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            return False
    return True

#Paramêtro da função, lista que vai receber os números primos, e primos alternados
n = 20 
primos = []
primos_alternados = []

#Iteramos a váriavel a partir do 2, que é primo, até o paramêtro estabelecido.
#'+ 1' novamente pra tratar o índice.
#Se a função retornar verdadeiro, o número é primo e então adicionamos 'num' a lista de primos.
for num in range(2, n + 1):
    if is_primo(num):
        primos.append(num)
        
print(f'Todos os números primos de 1 até {n}: {primos}')

#iteramos o índice de 0 até o comprimento da lista 'primos', pulando de 2 em 2.
#Ao iterar a lista adicionamos os números 'alternados' a lista 'alternada'.
#Poderiamos usar a linha 'primos_alternados = primos[::2]', mas a intenção é praticar o for. :)
for i in range(0, len(primos), 2): 
    primos_alternados.append(primos[i])

print(f'Todos os números primos alternados de 1 até {n}: {primos_alternados}')