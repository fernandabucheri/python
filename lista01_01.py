'''1) Crie um script em Python que solicite o nome, altura e peso
de uma pessoa e mostre a seguinte mensagem: “João tem
90 kilos e altura de 1.78 e portanto o IMC é de 28.4”.'''

nome = input('digite o nome: ')
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

IMC = float(peso/(altura*altura))

print(f'{nome} tem {peso} kilos e altura de {altura} e portanto o IMC é de {IMC:.2f}')
#print('{} tem {} kilos e altura de {} e portanto o IMC é de {:.2f}'.format(nome,peso,altura,IMC)