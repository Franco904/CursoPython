maior = 0
menor = 10000

for i in range(1, 6):
    p = float(input(f'Informe o peso da {i}° pessoa: '))

    if p > maior:
        maior = p

    if p < menor:
        menor = p

print(f'{maior} é o maior peso dos informados')
print(f'{menor} é o menor peso dos informados')

