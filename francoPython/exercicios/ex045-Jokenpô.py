import random
from time import sleep

print('\nJogar Jokenpô: \n')

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

continuar = 's'

escolhaComp = random.choice([pedra, papel, tesoura])

while continuar == 's':

    escolhaJog = input('Olá jogador! Escolha entre pedra, papel e tesoura: ').strip()

    if escolhaJog != 'pedra' and escolhaJog != 'papel' and escolhaJog != 'tesoura':
        print('JO')
        sleep(0.5)
        print('KEN')
        sleep(0.5)
        print('PO!!!')
        sleep(0.5)

        print('Esta opção não existe!')

    elif escolhaComp == pedra and escolhaJog == 'pedra'.lower() or escolhaComp == papel and escolhaJog == 'papel'.lower() or escolhaComp == tesoura and escolhaJog == 'tesoura'.lower():
        print('JO')
        sleep(0.5)
        print('KEN')
        sleep(0.5)
        print('PO!!!')
        sleep(0.5)

        print(f'\nEmpate!\n')
        print(f'Escolha do jogador: {escolhaJog}')
        print(f'Escolha do computador: {escolhaComp}')

    elif escolhaComp == pedra and escolhaJog == 'tesoura'.lower() or escolhaComp == papel and escolhaJog == 'pedra'.lower() or escolhaComp == tesoura and escolhaJog == 'papel'.lower():
        print('JO')
        sleep(0.5)
        print('KEN')
        sleep(0.5)
        print('PO!!!')
        sleep(0.5)

        print(f'\nVocê perdeu!\n')
        print(f'Escolha do jogador: {escolhaJog}')
        print(f'Escolha do computador: {escolhaComp}')

    else:
        print('JO')
        sleep(0.5)
        print('KEN')
        sleep(0.5)
        print('PO!!!')
        sleep(0.5)

        print(f'\nVocê ganhou!\n')
        print(f'Escolha do jogador: {escolhaJog}')
        print(f'Escolha do computador: {escolhaComp}')

    continuar = input('\nDeseja continuar jogando (s/n)? ').lower()

print('Foi uma boa partida! Até logo!')