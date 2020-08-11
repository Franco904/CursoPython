soma =  0

for i in range(1, 501):
    if i % 3 == 0:
        soma = soma + i

print(f'\nSoma dos números de 1 a 500: {soma}')