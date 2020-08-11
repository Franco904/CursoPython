p = int(input('Digite o primeiro termo para a progressão aritmética: '))
r = int(input('Digite a razão da progressão: '))

print('\nProgressão Aritmética:\n')

i = 1

while i <= 10:

    print(f'{p}', end=' ➙ ')
    p += r
    i += 1

print('Fim')