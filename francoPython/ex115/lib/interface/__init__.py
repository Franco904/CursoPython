def lin(tam=40):
    print('=' * tam)


def cabeçalho(msg):
    lin()
    print(msg)
    lin()


def leiaInt(entrada):
    while True:
        try:
            n = int(input(entrada))
        except (ValueError, TypeError):
            print('\033[31mErro! Idade inválida!\033[m')
            continue
        except KeyboardInterrupt:
            print('Você encerrou o programa na letura de dados.')
            return 0
        else:
            return n


def menu():
    lin()
    print('MENU PRINCIPAL'.center(40))
    lin()

    print('\033[36m[1]\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[36m[2]\033[m - \033[34mCadastrar uma nova pessoa\033[m')
    print('\033[36m[3]\033[m - \033[34mSair do programa\033[m')

    lin()
