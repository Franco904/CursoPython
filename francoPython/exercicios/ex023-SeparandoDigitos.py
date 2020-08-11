num = input('Digite um número de 4 dígitos: ')

if len(num) == 4:

    unidade = num[3]
    dezena = num[2]
    centena = num[1]
    milhar = num[0]

    print(f'\nUnidade: {unidade}')
    print(f'Dezena: {dezena}')
    print(f'Centena: {centena}')
    print(f'Milhar: {milhar}')

else:

    print('\nInsira um número de 4 dígitos!')