#crie e jogue o arquivo musica.mp3 pra pasta python-basic

import pygame 
import time

pygame.init()

# 1. Configurar o mixer (opcional, mas recomendado)
pygame.mixer.init()

# 2. Carregar a música
pygame.mixer.music.load('musica.mp3')

# 3. Iniciar a reprodução
pygame.mixer.music.play()

# 4. Criar um loop principal para manter o programa ativo
# O loop roda enquanto a música estiver sendo reproduzida
while pygame.mixer.music.get_busy():
    # Isso impede que o loop consuma 100% da CPU e permite que o SO
    # processe o áudio e outras tarefas.
    time.sleep(1) 

# 5. Parar o mixer e encerrar o Pygame após a música terminar
pygame.mixer.quit()
pygame.quit()