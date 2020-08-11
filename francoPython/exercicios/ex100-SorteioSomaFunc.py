from random import randint
from time import sleep

def sorteia(lista):
    print('Sortendo números...')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(numeros[i], end=' ')
        sleep(0.3)


def somaPar(lista):
    soma = 0

    for i, v in enumerate(numeros):
        if v % 2 == 0:
            soma += v

    print(f'\nLista de valores sorteados: {lista}')
    print(f'Soma dos números pares da lista: {soma}')


# Programa principal

numeros = list()
sorteia(numeros)
somaPar(numeros)
