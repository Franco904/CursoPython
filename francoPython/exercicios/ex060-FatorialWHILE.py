num = int(input('Informe um número: '))

fat = 1

while num > 0:

    fat = fat * num
    num = num - 1

print(f'Fatorial do número: {fat}')