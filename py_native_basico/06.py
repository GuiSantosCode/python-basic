print('Exercise 6: Display numbers divisible by 5')

num_lista = [10, 20, 33, 46, 55]

print(f'A lista fornecida é: {num_lista}')

for num in num_lista:
    if num % 5 == 0:
        print(num)