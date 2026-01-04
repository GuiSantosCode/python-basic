#(dicionario)

print('------ Ficha de herói 🛡️ ------ ')

ficha_heroi = {'nome': 'Legolas', 
               'classe': 'Elfo',  
               'vida': 100,       
               'ouro': 1000}      
 
print(f'Nome:', ficha_heroi['nome'])
print(f'Vida:', ficha_heroi['vida'])

print(f'''\n-Vilão: POW!!! (desfere um golpe)
-Herói: Arghh!

        ----------------
        Dano sofrido: 20
        ----------------\n''')

ficha_heroi['vida'] -= 20

print(f'Nome:', ficha_heroi['nome'])
print(f'Vida:', ficha_heroi['vida'])

print('\nSeu herói subiu de nível!\n')

ficha_heroi['nivel'] = 1
ficha_heroi['nivel'] += 1

print(ficha_heroi)