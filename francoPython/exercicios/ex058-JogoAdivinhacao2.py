import random

acertou = False
palpites = 0

while not acertou:

    print('\nVou pensar em um número entre 0 e 5 e você terá de adivinhá-lo!')
    numGerado = random.randint(0, 5)
    num = int(input('\nPronto! Qual o seu palpite? '))

    if num == numGerado:
        print(f'Você ganhou! {num} é o mesmo número que eu estava pensando!')
        acertou = True

    else:
        palpites += 1
        print(f'Que pena, o número que pensei foi {numGerado} ao invés de {num}!')

print(f'Você deu {palpites + 1} palpites até acertar!')