num = int(input('Informe um número: '))

fat = 1

for i in range(1, num + 1):

    fat = fat * i

print(f'Fatorial do número: {fat}')