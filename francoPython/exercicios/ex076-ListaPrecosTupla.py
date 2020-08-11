listagem = ('Lápis', 2.00, 'Frango Assado', 40.90, 'Panetone', 11.49,
            'Álcool Gel', 37.50, 'Caderno 12 Matérias', 16.00, 'Borracha', 3.00,
            'Cola Bastão', 6.50)

print('\n')
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for p in range(0, len(listagem)):

    if p % 2 == 0:
        print(f'{listagem[p]:.<30}', end='')

    else:
        print(f'R$ {listagem[p]:>7.2f}')

