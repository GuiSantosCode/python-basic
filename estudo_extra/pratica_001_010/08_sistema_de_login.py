print('Sistema de Login Simples (Foco: Dicionários + Funções)')

usuarios_cadastrados = {'admin': 'mestre',
                        'player1': 'guerreiro'}

senha_atual = '1234'

def verificar_acesso(nome_usuario, senha_usuario):
    if nome_usuario in usuarios_cadastrados:
        if senha_usuario == senha_atual:
            return f'Acesso garantido! Cargo: {usuarios_cadastrados[nome_usuario]}'
        else: 
            return f'Senha incorreta!'
    else:
        return f'Usuário não encontrado!'

nome_usuario_input = input('Digite seu usuário: ').lower()  
senha_usuario_input = input('Digite sua senha: ').lower()

print(verificar_acesso(nome_usuario_input, senha_usuario_input))