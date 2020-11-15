'''4) Desenvolva um programa que solicite o primeiro número
de uma PA e sua razão. O programa deve imprimir os 10
primeiros termos.'''

primeiro = int(input('Digite o primeiro termo da PA: '))
razão = float(input('Digite a razão da PA: '))

for i in range(0,10):
    n_termo = primeiro + i*razão
    print(f'O {i+1} termo da PA é {n_termo}')