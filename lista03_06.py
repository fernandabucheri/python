'''6) Faça um programa que calcule a soma os números
impares e múltiplos de 3 que se encontram no intervalo
de 1 até 500'''

soma = 0
for i in range(0,501,3):
    if(i % 2 != 0):
        soma = soma + i
print(f'A soma é {soma}.')
