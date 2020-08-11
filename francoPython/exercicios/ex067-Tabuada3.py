while True:
    num = int(input('\nInforme um número qualquer (digite qualquer valor negativo para finalizar o programa): '))

    if num < 0:
        print(f'\nPrograma finalizado. Tenha um bom dia!\n')
        break

    if num >= 0:
        print(f'\nA tabuada de {num} é:\n')

        for i in range (1, 11):

            print(f'{num} * {i} = {num * i}')