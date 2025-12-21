print('Exercício 17: Gere uma série de Fibonacci com até 15 termos.')

t1, t2 = 0, 1

for i in range(15):
    print(t1, end = ' ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3