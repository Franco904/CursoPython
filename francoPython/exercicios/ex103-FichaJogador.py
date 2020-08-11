def lin():
    print('=' * 30)


def ficha(nome, gols):

    return f'O jogador {nome} fez {gols} gols(s) no campeonato.'


nome = input('Nome do jogador: ').title().strip()
gols = input('Número de gols marcados: ').strip()

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if nome == '':
    nome = '<deconhecido>'

print(ficha(nome, gols))





















