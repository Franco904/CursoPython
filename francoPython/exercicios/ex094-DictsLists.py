from time import sleep

dados = dict()
lista = list()
pessoas = media = i = 0

continuar = 's'

while continuar in 'sSsimSIM':

    dados['nome'] = input('Nome: ').title().strip()
    dados['sexo'] = input('Sexo (M ou F): ').strip().upper()

    while dados['sexo'] not in 'mfMF':
        dados['sexo'] = input('Resposta inválida. Sexo (M ou F): ').strip()

    dados['idade'] = int(input('Idade: '))

    lista.append(dados.copy())
    pessoas += 1
    i += 1

    media = media + dados['idade']

    continuar = input('Deseja continuar cadastrando dados? (S/N): ').strip()

    while continuar not in 'snSNsimnaoSIMNAO':
        continuar = input('Resposta inválida. Deseja continuar cadastrando dados? (S/N): ').strip()

media = media / i

print('\n== DADOS LEVANTADOS ==\n')
sleep(1)
print(f'Número de pessoas cadastradas: {pessoas}') # 1) QUANTAS PESSOAS FORAM CADASTRADAS
sleep(1)
print(f'Média de idade do grupo: {media:.2f}') # 2) A MÉDIA DE IDADE DO GRUPO
sleep(1)

print(f'As mulheres cadastradas foram: ', end=' ') # 3) UMA LISTA COM TODAS AS MULHERES CADASTRADAS
for i in range(0, pessoas):
    if lista[i]['sexo'] in 'fF':
        print(lista[i]["nome"], end='.. ')

sleep(1)
print()

print(f'Pessoas com idade acima da média ({media:.2f}): ', end=' ') # 4) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA
for i in range(0, pessoas):
    if lista[i]['idade'] > media:
        print(lista[i]["nome"], end='.. ')
