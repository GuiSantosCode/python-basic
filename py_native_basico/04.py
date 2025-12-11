print('Exercício 4: Remover os primeiros ncaracteres de uma string')

def remove_chars(word, n): 
    return word [n:]
    
input_word = input('Escreva uma palavra: ')
input_n = int(input('Escreva quantos caracteres quer tirar: '))

print(remove_chars(input_word, input_n))