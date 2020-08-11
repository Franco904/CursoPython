tabelaBr = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
            'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
            'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense',
            'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('\n')

print('=' * 30)
print(f'Tabela Brasileirão 2019: {tabelaBr}')
print('=' * 30)

print('-' * 30)
print(f'Os 5 primeiros colocados a tabela são: {tabelaBr[:5]}')
print('-' * 30)
print(f'Os 4 últimos colocados da tabela são: {tabelaBr[-4:]}')
print('-' * 30)
print(f'Times em ordem alfabética: {sorted(tabelaBr)}')
print('-' * 30)
print(f'A Chapecoense está no {tabelaBr.index("Chapecoense") + 1}º lugar')
print('-' * 30)
