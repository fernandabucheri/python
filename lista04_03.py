'''
3) Crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela com a formatação correta.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = float(input(f'Digite o número que está na linha {i} e coluna {j} da matriz 3 x 3: '))


for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end='')
    print('')
