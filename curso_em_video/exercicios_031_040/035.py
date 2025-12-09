print('------ Pode ser triângulo? -----')
#a soma de duas retas tem que ser maior que a terceira reta, pra formar um triângulo

a = float(input('Qual o comprimento da reta A: '))
b = float(input('Qual o comprimento da reta B: '))
c = float(input('Qual o comprimento da reta C: '))

if (a + b > c):
    print('Pode ser triângulo!!!')
else: 
    print('Não pode ser triângulo!!!')