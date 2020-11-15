'''1) Escreva um programa que pergunte a velocidade do carro
de um usuário. Caso ultrapasse 80 km/h, exiba uma
mensagem dizendo que o usuário foi multado. Nesse
caso, exiba o valor da multa, cobrando 5 reais por Km
acima de 80Km/h.'''

velocidade = float(input('Digite a velocidade do veículo: '))
if(velocidade>80):
    valor = (velocidade-80)*5
    print(f'Você foi multado! O valor da multa é R$ {valor:.2f}.')
else:
    print('O veículo está dentro da velocidade permitida')