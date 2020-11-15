'''
Escreva uma função que receba dois números e retorne True
se o primeiro número for múltiplo do segundo. '''

def verificar(x,y):
    if(x % y == 0):
        return True
    else:
        return False
    
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print(verificar(n1,n2))