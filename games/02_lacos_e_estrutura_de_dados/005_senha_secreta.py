#(while True + break + validacao)

print('\n------ Senha Secreta da Base 👽 ------\n')

correct_password = "area51"

while True:
    user_password = (input('Digite a senha: '))
    if user_password == correct_password:
        print('Acesso Autorizado!')
        break
    else: 
        print('Senha Inválida, Tente novamente.')