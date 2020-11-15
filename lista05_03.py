'''
3) Crie uma matriz 4 x 3 de números aleatórios inteiros no
intervalo -5 a 5 e armazene em uma variável “mat”

a) Escreva um comando que retorna o valor absoluto dos
elementos dessa matriz.
b) Escreva um comando que retorna o seno dos valores
contidos na primeira linha dessa matriz.
c) Escreva um comando que retorne o valor máximo das
colunas da matriz
d) Calcule a soma dos elementos em cada coluna da matriz
e) Calcule a soma dos elementos em cada linha da matriz
f) Calcule o produto entre os elementos de cada coluna da
matriz. Dica: procure no google como resolver isso
'''

import numpy as np

mat = np.random.randint(0,10,(4,3)) - 5

#a
print('a')
print(np.absolute(mat))

#b
print('b')
senos = mat[0:4][1]
print(mat[0:4][1])
print(np.sin(senos))

#c
print('c')
print(mat.max(0))

#d
print('d')
print(mat.sum(0))

#e
print('e')
print(mat.sum(1))

#f
print('f')
print(mat.prod(0))