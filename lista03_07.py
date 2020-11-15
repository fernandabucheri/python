'''
7) Escreva um script que exibe a seguinte tábua de
multiplicação na tela:
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
'''

for i in range(1,6):
    for j in range(i,i*i+1,i):
        print(str(j) + ' ',end='') #end para não quebrar a linha
    print('') #Coloca esse para quebrar a linha

    #precisa colocar o str para poder concatenar com o ' ', senão da erro
    #não da pra concatenar um int com string, tem que ser duas strings