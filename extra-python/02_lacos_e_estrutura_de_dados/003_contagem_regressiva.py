#while + import time

print('------ Lançamento de Foguete! ------')

import time

lancar = (input('Aperte qualquer tecla para lançar: '))
tempo = 10
voo = 10

while tempo > 0:
    print(f'{tempo}')
    tempo -= 1
    time.sleep(1)

print(f'''          .            .        .         .             .
            .            LANÇAMENTO!!!            .       
    .                .           .                     .
         🌎      . --->       🚀      --->       🌕    .
        .               .                .             .
                .           .           .       
''')