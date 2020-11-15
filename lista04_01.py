'''1) Faça um programa que leia o nome e nota da P1 de vários
alunos guardando tudo em uma lista e no final mostre:
a. Quantas alunos foram cadastradas
b. O nome do aluno com maior nota
c. O nome da pessoa menor nota
d. O nota média da sala.'''

lista = []
novonome = 's'
i = soma = 0
menor = 10
maior = 0

while(novonome == 's'):
    i += 1
    nome = input('Digite o nome do aluno: ')
    lista.append(nome)

    nota = float(input('Digite a nota do aluno: '))
    soma += nota
    lista.append(nota)

    if(nota < menor):
        menor = nota
        menor_nome = nome
    if(nota > maior):
        maior = nota
        maior_nome = nome

    novonome = input('Deseja cadastrar um novo aluno? [S/N] ')

print(f'O aluno com menor nota é {menor_nome}. Sua nota foi {menor:.2f}')
print(f'O aluno com maior nota é {maior_nome}. Sua nota foi {maior:.2f}')
print(f'A média da P1 da sala é {(soma/i):.2f}.')