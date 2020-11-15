'''
2) Escreva uma função chamada maxnum que retorne o maior
número de um conjunto de números. Utilize
empacotamento para fazer a função.
'''

def maxnum(*numeros):
    m = max(*numeros)
    return m

numeros = []

N = int(input('Digite a quantidade de números a serem digitados: '))

for i in range(1, N+1):
    numeros.append(float(input(f'Digite o {i}º valor do conjunto de números: ')))

print(f'O maior valor do conjunto de números digitado é {maxnum(numeros)}')