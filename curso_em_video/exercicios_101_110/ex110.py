try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    resultado = a / b
except(ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except(ZeroDivisionError):
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {resultado:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')