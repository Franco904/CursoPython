from time import sleep


def quebra():
    print('\n')


def lin():
    print('=' * 30)


def contador(inicio, fim, passo):

    if (inicio > fim and passo > 0) or (inicio < fim and passo < 0):
        passo = -passo

    if passo == 0:
        passo = 1

    quebra()

    print(f'Contagem de {inicio} até {fim} contando de {abs(passo)} em {abs(passo)}:')

    for i in range(inicio, fim + passo, passo):
        print(i, end=' ')
        sleep(0.3)


# Programa principal

contador(0, 10, 1)
contador(10, 0, -2)

quebra()

inicio = int(input('Valor inicial para contagem personalizada: '))
fim = int(input('Valor final da contagem: '))
passo = int(input('Razão da contagem: '))

contador(inicio, fim, passo)
quebra()
