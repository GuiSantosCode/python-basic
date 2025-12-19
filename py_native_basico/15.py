def exponencial(base, expoente):
    resultado = 1
    while expoente > 0:
        resultado *= base
        expoente -= 1
    return resultado

print(exponencial(5, 3)) 