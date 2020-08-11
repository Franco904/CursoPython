from time import sleep

jogador = dict()
partidas = list()
time = list()
quantGols = 0
continuar = 's'

while continuar in 'sSsimSIM':

    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ').strip().title()
    total = int(input('Partidas jogadas no campeonato: '))
    partidas.clear()

    for i in range(0, total):
        partidas.append(int(input(f'Quantidade de gols feitos na {i + 1}ª partida: ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    continuar = input('Deseja continuar cadastrando dados? (S/N): ').strip()

    while continuar not in 'snSNsimnaoSIMNAO':
        continuar = input('Resposta inválida. Deseja continuar cadastrando dados? (S/N): ').strip()

print('\n')
print('=' * 40)
print(f'{"Cód":<4}{"Nome":<6}{"Gols":>12}{"Total":>15}')

for k, v in enumerate(time):
    print(f'{k:<4}', end='')

    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:

    print('=' * 40)
    o = int(input('Deseja mostrar os dados de qual jogador? (999 para interromper): '))
    print('=' * 40)

    if o == 999:
        print('Encerrando o programa...')
        break

    if o >= len(time):
        print('Erro! Não existe jogador com o código indicado!')

    else:
        print('=' * 40)
        print(f'== DADOS DO JOGADOR - {time[o]["nome"]} ==')

        for i, g in enumerate(time[o]["gols"]):
            print(f'    No {i + 1}º jogo fez {g} gols')
        print('=' * 40)
print('\nFim. Tenha um ótimo dia!')