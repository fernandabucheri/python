''' 4) Escreva uma função chamada área_quad que recebe os
lados de um retângulo e retorne sua área.
'''

def área_quad (x,y):
    return x*y

x = float(input('Digite o lado maior do retângulo: '))
y = float(input('Digite o lado menor do retângulo: '))
print(f'A aréa do retângulo é {área_quad(x,y)}')