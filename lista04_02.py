'''
2) Crie um programa onde o usuário possa digitar 10 valores
numéricos e cadastre-os em 2 listas separadas. Sendo a
primeira contendo números primos e segunda não
primos.
'''

listnaoprimos = []
listprimos = []

for i in range(0, 10):
    numero = int(input('Digite um número inteiro: '))
    p = True
    for j in range(2, numero):
        if(numero % j == 0):
            print(f'O número {numero} não é primo.')
            listnaoprimos.append(numero)
            p = False
            break
    if(p):
        print(f'O numéro {numero} é primo.')
        listprimos.append(numero)

print('Os números primos digitados são: ')
print(listprimos)
print('Os numéros não primos digitados são: ')
print(listnaoprimos)
