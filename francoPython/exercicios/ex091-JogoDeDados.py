from random import randint
from time import sleep
from operator import itemgetter

jogadores = list()

for i in range(0, 4):
    j = input(f'Jogador {i + 1}: ').title().strip()
    jogadores.append(j)

jogo = {jogadores[0]: randint(1, 6),
        jogadores[1]: randint(1, 6),
        jogadores[2]: randint(1, 6),
        jogadores[3]: randint(1, 6),
        }

print('=' * 30)

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)

print('=' * 30)
print('== Ranking Final ==')
print('\n')

for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)