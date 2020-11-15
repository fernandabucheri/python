'''2) Escreva uma expressão que possa selecionar apenas os
elementos de índice par em um vetor, independente do
tamanho do vetor. Teste essa expressão em alguns vetores da
sua escolha'''

import numpy as np 

size = int(input( ))

Vetor = np.arange(0, size)

for i in range(0, size, 2):
    print(f'Vetor[{i}] = {Vetor[i]}')
    