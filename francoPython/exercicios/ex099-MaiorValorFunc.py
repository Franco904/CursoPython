from time import sleep


def lin():
    print('=' * 30)


def maior(* num):

    maiorvalor = 0

    print('Analisando os valores passados...')

    for i, v in enumerate(num):
        print(v, end=' ')
        sleep(0.5)

        if i == 1:
            maiorvalor = v

        if v > maiorvalor:
            maiorvalor = v

    print(f'-- Foram informados {len(num)} valores ao todo.')

    print(f'O maior valor informado foi {maiorvalor}')


# Programa principal

lin()
maior(3, 4, 50, 30, 12)
lin()
maior(2, 5, 14, 9)
lin()
maior(1, 2, 3, 4, 5)
lin()
maior(9, 0, 7)
lin()
maior(3, 8)
lin()