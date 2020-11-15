'''1) Crie uma rotina que solicite ao usuário dois lados de um
triângulo e ângulo , em graus, entre eles e retorna o
comprimento do terceiro lado. Use a lei dos cossenos.'''

import math

b = float(input('Digite o primeiro lado do triângulo: '))
c = float(input('Digite o segundo lado do triângulo: '))
ângulo = float(input('Digite o ângulo entre eles, em graus: '))

a = math.sqrt((b**2)+(c**2)-(2*b*c*math.cos(math.radians(ângulo))))

print(f'O comprimento do terceiro lado é {a:.2f} cm')