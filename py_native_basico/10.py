num = int(input('Digite um número: '))

while num > 0:
    num_inverso = num % 10
    print(num_inverso)
    num = num // 10
