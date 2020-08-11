lista = []
mai = men = 0

for i in range(0, 5):
    lista.append(int(input(f'Digite o {i + 1}º número: ')))

    if i == 1:
        mai = men = lista[i]

    else:
        if lista[i] > mai:
            mai = lista[i]

        if lista[i] < men:
            men = lista[i]

print(f'\nLista de números: {lista}')

print(f'O maior valor na lista é {mai} na(s) posição(ões) ', end='')

for i, n in enumerate(lista):
    if n == mai:
        print(f'{i}... ', end='')
print()

print(f'O menor valor na lista é {men} na(s) posição(ões) ', end='')

for i, n in enumerate(lista):
    if n == men:
        print(f'{i}...', end='')
print()