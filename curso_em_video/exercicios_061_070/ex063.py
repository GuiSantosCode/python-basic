n = int(input('Quantos termos você quer adicionar? '))
t1, t2 = 0, 1
i = 0
print(t1, t2, end=' ')

while i < n - 2:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3, end=' ')
    i += 1