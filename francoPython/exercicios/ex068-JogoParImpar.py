import random

v = 0

while True:
    print('\nJogar "Par ou Ímpar"')

    escolhaJog = input('\nEscolha uma opção entre Par ou Ímpar: ').strip()

    jog = int(input('\nLance um número (entre 1 e 5): '))
    comp = random.randint(1, 5)

    soma = jog + comp

    print(f'Número jogado pelo computador: {comp}')

    if escolhaJog in 'parPARPar':

        if soma % 2 == 0:
            print('\nVocê ganhou!')
            v += 1

        else:
            print(f'Você perdeu!\nVitórias consecutivas: {v}')
            break

    elif escolhaJog in 'imparIMPARImpar':

        if soma % 2 != 0:
            print('\nVocê ganhou!')
            v += 1

        else:
            print(f'Você perdeu!')
            print(f'\nVitórias consecutivas: {v}')
            break