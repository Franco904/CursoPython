p = int(input('Digite o primeiro termo para a progressão aritmética: '))
r = int(input('Digite a razão da progressão: '))

print('\nProgressão Aritmética:\n')

dec = p + (10 - 1) * r

for i in range(p, dec + r, r):
    print(i, end = ' ➙ ')

print('Fim')