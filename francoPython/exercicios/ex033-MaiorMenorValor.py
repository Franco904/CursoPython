num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite mais outro número: '))

menor = num1
maior = num1

#Verificando qual número é o menor
if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3

print(f'{menor} é o menor número entre os três')

# Verificando qual número é o maior
if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3

print(f'{maior} é o maior número entre os três')
