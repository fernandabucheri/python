'''Crie uma rotina que solicite uma frase ao usuário e retorne
o número de caracteres na frase e o número de espaços.'''

frase= input('Digite uma frase: ').strip()
tamFrase = len(frase)
nspaces = frase.count(' ')
print(f'A frase digitada tem {tamFrase} caracteres e {nspaces} espaços')