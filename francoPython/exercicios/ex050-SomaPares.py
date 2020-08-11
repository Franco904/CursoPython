soma = 0

for i in range(1, 7):
    num = int(input(f'Informe o {i}° número: '))

    if num % 2 == 0:
        soma = soma + num

print(f'\nSoma dos números pares informados: {soma}')
