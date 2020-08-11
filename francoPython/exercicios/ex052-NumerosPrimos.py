num = int(input('Informe um número: '))

div = 0

for i in range (1, num + 1):
    if num % i == 0:
        print(f'\033[33m', end = '') # Números múltiplos em vermelho
        div += 1

    else:
        print(f'\033[m', end = '') # Demais números em branco

    print(i)

if div == 2:
    print(f'\n{num} é primo pois é divisível por um e ele mesmo!')

else:
    print(f'\n{num} não é primo pois é divisível por mais de dois números!')
