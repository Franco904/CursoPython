lista = []
continuar = 's'

while True:

    num = int(input('Digite um valor: '))

    if num not in lista:
        lista.append(num)
        print(f'Valor inserido na lista!')

    else:
        print(f'{num} está duplicado! ', end='')

    continuar = input('Deseja continuar incluindo números? (S/N): ').strip()[0]

    while continuar not in 'sSnN':
        continuar = input('Deseja continuar incluindo números? (S/N): ').strip()[0]


    if continuar in 'nN':
        break

lista.sort()
print(f'\nVocê digitou os valores {lista}')