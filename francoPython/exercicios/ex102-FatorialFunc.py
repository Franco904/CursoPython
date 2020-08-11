def lin():
    print('=' * 30)


def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: Número n a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        f *= i
        i += 1

    return f

lin()
num = int(input('Informe um número: '))
lin()
print(fatorial(num, show=True))
lin()