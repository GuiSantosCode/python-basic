print('----- TIPOS -----')
n = input('Digite algo: ')

print(f'''É de que tipo? {type(n)}
É numérico? {n.isnumeric()}
É alfabético?  {n.isalpha()}
É alfanumérico?  {n.isalnum()}''')