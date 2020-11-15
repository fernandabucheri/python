'''
5) Escreva uma função chamada área_triang que receba a
base e a altura de um triangulo e retorne sua aréa.
'''
def área_triang(b,h):
    return (b*h)/2

base = float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))
print(f'A área do triângulo é {área_triang(base,altura)}')