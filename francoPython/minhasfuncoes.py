from math import sqrt
from time import sleep


def cbrt(num):

    return num ** (1/3)


def cabecalho():

    print('=' * 30)
    print('Iniciando Calculadora...')
    print('=' * 30)
    sleep(0.75)


def menu():

    num = int(input('Digite um número: '))

    print('=' * 30)
    print('[ 1 ] Raíz quadrada')
    print('[ 2 ] Raíz cúbica')
    print('=' * 30)

    o = int(input('Opção: '))

    while True:
        if o == 1:
            print(f'Raíz quadrada: {sqrt(num):.2f}')
            break

        if o == 2:
            print(f'Raíz cúbica: {cbrt(num):.2f}')
            break

        else:
            o = int(input('\033[31mErro!\033[m Opção: '))
            continue

    return o