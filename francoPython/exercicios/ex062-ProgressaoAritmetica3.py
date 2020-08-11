p = int(input('Digite o primeiro termo para a progressão aritmética: '))
r = int(input('Digite a razão da progressão: '))

print('\nProgressão Aritmética:\n')

i = 1
total = 0
termos = 10

while termos != 0:

    total += termos
    while i <= total:

        print(f'{p}', end=' ➙ ')
        p += r
        i += 1

    print('Pausa')
    termos = int(input('\nQuantos termos deseja mostrar a mais? '))

print(f'\nProgressão finalizada com um total de {total} termos exibidos.')