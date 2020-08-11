dados = list()
nomePeso = list()
continuar = 's'
i = 1
pessoas = maiorPeso = menorPeso = 0
nomeMaiorP = nomeMenorP = ''

while continuar in 'sSsimSIM':

    dados.append(input(f'\nDigite o nome da {i}ª pessoa: ').title().strip())
    dados.append(input(f'Digite o peso da {i}ª pessoa: '))
    pessoas += 1

    if i == 1:
        maiorPeso = menorPeso = dados[1]
        nomeMaiorP = nomeMenorP = dados[0]

    if dados[1] > maiorPeso:
        maiorPeso = dados[1]
        nomeMaiorP = dados[0]

    if dados[1] < menorPeso:
        menorPeso = dados[1]
        nomeMenorP = dados[0]

    nomePeso.append(dados[:])
    dados.clear()

    continuar = input('\nDeseja continuar cadastrando dados? (S/N): ').strip()

    while continuar not in 'SNsnSIMNAOsimnao':
        continuar = input('Deseja continuar cadastrando dados? (S/N): ').strip()

    i += 1

print(f'\nTotal de pessoas cadastradas: {pessoas}')

for p in nomePeso:
    if p[1] == maiorPeso:
        print(f'O maior peso foi de {p[1]} kg. Peso referente a {nomeMaiorP}.')

    if p[1] == menorPeso:
        print(f'O menor peso foi de {p[1]} kg. Peso referente a {nomeMenorP}.')
