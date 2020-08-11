import random
from time import sleep

palpites = list()
jogos = list()
n = int(input('Quantos jogos deseja realizar o sorteio? '))
tot = 1

while tot <= n:
    i = 0
    while i <= 6:

        nRandom = random.randint(1, 60)

        if nRandom not in palpites:
            palpites.append(nRandom)
            i += 1

    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()

    tot += 1

print('\n')
print('=' * 3, f' Sorteando jogos ', '=' * 3)

for i, lista in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i + 1}: {lista}')

print('=' * 3, f' Jogos sorteados! ', '=' * 3)
print('\n')
