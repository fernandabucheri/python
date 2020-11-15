'''4) Faça um programa que leia o nome completo de uma
pessoa e imprime somente o primeiro e o último nome
separadamente.'''

nome= input('Digite seu nome completo: ')
f = nome.split()
print(f[0], f[len(f) - 1])