tNum = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

continuar = 'S'

while continuar in 'Ss':

    while True:

        num = int(input('Digite um número entre 0 e 20: '))

        if 0 <= num <= 20:
            print(f'Você digitou o número {tNum[num]}.')

            continuar = input('Deseja continuar o programa? (S/N): ').strip()[0]
            break

        print('Tente novamente. ', end='')

print('Até mais! :)')