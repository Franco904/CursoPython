def leiadinheiro(dinheiro):

    valor = 0

    while True:

        p = str(input(dinheiro)).replace(',', '.').strip()

        if p.isalpha() or p == '':
            print(f'\033[0;31mErro! \"{p}\" não é um preço válido.\033[m')

        else:
            valor = float(p)
            break

    return valor

