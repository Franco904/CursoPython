def leiaint(entrada):
    while True:
        try:
            n = int(input(entrada))
        except (ValueError, TypeError):
            print('\033[31mErro! O dado não é um inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print('Você encerrou o programa na letura de dados.')
            return 0
        else:
            return n


def leiafloat(entrada):
    while True:
        try:
            n = float(input(entrada))
        except (ValueError, TypeError):
            print('\033[31mErro! O dado não é um real!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mVocê encerrou o programa na leitura de dados.\033[m')
            return 0
        else:
            return n


inteiro = leiaint('Digite um número inteiro: ')
print('=' * 30)
real = leiafloat('Digite um número real: ')
print('=' * 30)
print(f'Você digitou o número inteiro {inteiro}')
print(f'Você digitou o número real {real}')




