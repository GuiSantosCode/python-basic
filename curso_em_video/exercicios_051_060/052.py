num = int(input('Digite um número: '))
qntd_de_divisoes = 0

for i in range(1, num + 1):
    if num % i == 0:
        qntd_de_divisoes += 1

if qntd_de_divisoes == 2:
    print('Primo!')
else: 
    print('Não é primo')