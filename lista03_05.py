'''5) Escreva um programa que pergunte o deposito inicial e a
taxa de Juros de uma poupança. Exiba os valores mês a
mês para os 24 primeiros meses. No final deve imprimir o
total de ganho com juros no período.'''

deposito = float(input('Qual o valor do depósito inicial?: '))
taxajuros = float(input('Digite a taxa de juros em %: '))

taxajuros = 1 + taxajuros/100
dep_inicial = deposito
print(f'O valor no mês 0 e de {deposito:.2f} reais')
for i in range(1,25):
    deposito = deposito * taxajuros
    print(f'O valor do mês {i} é de {deposito:.2f} reais')

print(f'O total de ganho com juros no período foi de {deposito-dep_inicial:.2f} reais')