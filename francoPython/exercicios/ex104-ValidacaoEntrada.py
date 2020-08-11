def leiaInt(entrada):

    valor = 0

    while True:

        n = int(input(entrada))

        print(f'\033[0;31mErro! Digite um valor inteiro válido!\033[m')

        valor = int(n)
        break

    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')



