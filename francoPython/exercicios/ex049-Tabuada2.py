num = int(input('Informe um número qualquer: '))

print(f'\nA tabuada de {num} é:\n')

for i in range (1, 11):

    print(f'{num} * {i} = {num * i}')