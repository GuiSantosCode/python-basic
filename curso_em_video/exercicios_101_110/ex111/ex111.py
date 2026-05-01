from funcoes import efeito_cyberpunk

tentativas = 2

# Execução do efeito (cuidado com as velocidades muito altas, 1s por letra é bem lento!)
efeito_cyberpunk('O Desafio: "The Icebreaker"', 0.05)
efeito_cyberpunk('Você está tentando acessar um banco de dados da Arasaka.', 0.03)
efeito_cyberpunk('Decodifique o chip em 2 tentativas.', 0.03)
efeito_cyberpunk('3 8 9 5 4 1 0 5 4 6 33', 0.1)
efeito_cyberpunk('A ordem decresce', 0.05)
efeito_cyberpunk('Divisível por 3', 0.05)

while True:
    try:
        tentativa = int(input('Insira o código: '))
        if tentativa == 33963:
            print('Acesso concedido!')
            efeito_cyberpunk('Bem vindo a ARASAKA!', 0.1)
            break
        else: 
            tentativas -= 1
        if tentativas == 0:
            print('Acesso negado!')
            efeito_cyberpunk('Protócolo caçe o INIMIGO ativada!', 0.1)
            break
    except ValueError:
        print('Tipo de dado incorreto!')