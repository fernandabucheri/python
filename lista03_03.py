'''3) Escreva um programa que pergunte a distância que um
passageiro deseja percorrer em km. Calcule o preço da
passagem cobrando 0,50 por Km rodado para viagens até
200Km e 0,45 para viagens mais longas.'''


distancia = float(input('Digite a distância que deseja percorrer em KM: '))
if(distancia < 200):
    total = 0.50 * distancia
else:
    total = 0.45 * distancia

print(f'O valor da passagem é de R$ {total:.2f}')