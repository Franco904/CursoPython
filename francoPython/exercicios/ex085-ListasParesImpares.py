numeros = [[], []]
n = 0

for i in range(1, 8):

    n = int(input(f'Número {i}: '))

    if n % 2 == 0:
        numeros[0].append(n)

    else:
        numeros[1].append(n)


print(f'Pares: {sorted(numeros[0])}')
print(f'Impares: {sorted(numeros[1])}')