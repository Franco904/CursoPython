from time import sleep

jogador = dict()
partidas = list()
quantGols = 0

jogador['nome'] = input('Nome do jogador: ').strip().title()
jogador['partidas'] = int(input('Partidas jogadas no campeonato: '))

for i in range(0, jogador["partidas"]):
    partidas.append(int(input(f'Quantidade de gols feitos na {i + 1}ª partida: ')))
    quantGols += partidas[i]


jogador['quantGols'] = quantGols

print('== DADOS DO JOGADOR ==')

print(f'Nome do jogador: {jogador["nome"]}')
sleep(1)
print(f'Quantidade de partidas jogadas: {jogador["partidas"]}')
sleep(1)

for i in range(0, jogador["partidas"]):
    print(f'=>    Gols feitos na {i + 1}ª partida: {partidas[i]}')

sleep(1)

print(f'Total de gols marcados no campeonato: {jogador["quantGols"]}')

print(jogador)