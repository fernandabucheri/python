'''6) Crie uma função na qual calcula o valor do cos a partir da série
de Taylor (50 primeiros termos) e seno a partir da seguinte
identidade.
Obs: Fazer a serie utilizando for e utilizar a função
fatorial desenvolvida no exercício 1.
'''

import math

def fatorial (x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


def converter(n):
    rad = (n/180)*math.pi
    return rad

def cosseno(rad):
    n = converter(rad)
    cont = 0
    result = 1 
    while(cont < 50):
        cont += 1
        result += (((-1)**cont)*(n**(2 * cont)))/(fatorial(2 * cont))
    return round(result, 6)

def seno(n):
    result = 0
    result = math.sqrt(1 - (cosseno(n))**2)
    return round(result, 6)


x = int(input())

print(f'sen({x}º) = {seno(x)}, cos({x}º) = {cosseno(x)}')
