'''5) Escreva um script que pergunte a quantidade de Km
percorridos por um carro alugado pelo usuário e a
quantidade de dias pelo qual o carro foi alugado. Calcule o
preço a pagar sabendo que o carro custa 60 reais por dia e
15 centavos por Km rodado.'''

km = float(input('Qual a quantidade de KM percorridos? '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))

valordias = dias * 60
valorkm = km * 0.15

print(f'O carro foi utilizado {dias} dia(s) e rodou {km} KM. \nO valor a ser pago é de {valordias+valorkm}')
