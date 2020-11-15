'''
4) Faça um programa que leia o nome RA e média final de
uma aluno. Armazene todas as informações num
dicionário. No final programa deve imprimir as
informações do dicionário e situação do aluno
(reprovado, exame ou aprovado). Utilize as regras da
UNIFESP para definir a situação do aluno.
'''

notas = []
aluno = {}

novo = 's'
while(novo == 's'):
    aluno.clear()
    aluno['nome'] = str(input('Digite o nome do aluno: '))
    aluno['RA'] = int(input('Digite o RA do aluno: '))
    aluno['mf'] = float(input('Digite a média final do aluno: '))
    if(aluno['mf'] >= 6):
        aluno['situação'] = 'Aprovado'
    elif(aluno['mf'] >= 3 and aluno['mf'] < 6):
        aluno['situação'] = 'Exame'
    else:
        aluno['situação'] = 'Reprovado'
    notas.append(aluno.copy())
    novo = input('Deseja cadastrar um novo aluno? [S/N] ')

print(notas)
for i in notas:
    print(f'Nome: {i["nome"]}')
    print(f'RA: {i["RA"]}')
    print(f'Média final: {i["mf"]}')
    print(f'Situação: {i["situação"]}')
    print()

'''

nome = input('digite o nome do aluno: ')
media = float(input('digite a media final do aluno'))
aluno ={
    'nome':nome,
    'media':media
}
print(aluno)
if(media < 3):
    print('o aluno esta reprovado')
elif(media > 6):
    print('o aluno esta aprovado')
else:
    print('o aluno esta de exame')
    
'''