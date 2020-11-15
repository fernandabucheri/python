'''
1) Escreva uma função chamada fatorial para calcular o fatorial
de um número inteiro.
'''
def fatorial (x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f


N = int(input('Digite o número: '))
print(f'O fatorial de {N} é {fatorial(N)}.') 