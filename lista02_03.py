'''3) No sistema SI, a vazão de um fluido é medida em metros
cúbicos por segundo (m^3 /s). A medida do sistema inglês
de vazão, o pé cúbico por segundo (ft^3/s) é equivalente
a 0.028 m^3/s. Escreva uma rotina que pede ao usuário pela
vazão em metros cúbicos por segundo e converte essa vazão
para a unidade inglesa, exibindo o seguinte ao usuário:

Um fluxo de 15.2000 metros cúbicos por segundo
é equivalente a 542.8571 pés cúbicos por segundo'''
m3 = float(input('Digite a vazão em metros cúbicos por segundo: '))
ft3 = m3 / 0.028
print(f'Um fluxo de {m3:.4f} metros cúbicos por segundo é equivalente a {ft3:.4f} pés cúbicos por segundo')
