print('------ Hipotenusa ------')

cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))

hipotenusa = (cateto_oposto**2 + cateto_adjacente**2) ** (1/2)

print(f'Hipotenusa: {hipotenusa:.1f}')