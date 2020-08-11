import random

continuar = 's'

while continuar == 's':

    print('\nVou pensar em um número entre 0 e 5 e você terá de adivinhá-lo!')
    numGerado = random.randint(0, 5)
    num = int(input('\nPronto! Qual o seu palpite? '))

    if num == numGerado:
        print(f'Você ganhou! {num} é o mesmo número que eu estava pensando!')

    else:
        print(f'Que pena, o número que pensei foi {numGerado} ao invés de {num}!')

    continuar = input('\nDeseja continuar jogando (s/n)? ').lower()

print('Programa OFF')