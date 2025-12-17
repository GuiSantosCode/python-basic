num = int(input('Digite um número: '))

while num > 0:
    num_convertido = num % 10
    num = num // 10
    print(num_convertido)