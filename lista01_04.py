''' 4) Faça um script que calcule o aumento de salário. Ele deve
solicitar o valor do salário e a porcentagem de aumento.
Exiba o valor do aumento e do novo salário.'''

salarioatual = float(input('Digite o salário atual: '))
porcentagem = float(input('Digite a porcentagem do aumento: '))
novovalor = salarioatual + ((porcentagem/100)*salarioatual)

print(f'O novo salário com {porcentagem:.2f}% de aumento é {novovalor:.2f} ')