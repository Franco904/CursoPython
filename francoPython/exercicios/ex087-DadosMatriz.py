matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sTotal = sTC = maiorValorSL = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor na posição [{i}, {j}]: '))

print('=' * 30)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]:^5} ]', end='')

        if matriz[i][j] % 2 == 0:
            sTotal += matriz[i][j]

    print()

for i in range(0, 3):
    sTC += matriz[i][2]

for j in range(0, 3):

    if j == 0:
        maiorValorSL = matriz[1][j]

    if matriz[1][j] > maiorValorSL:
        maiorValorSL = matriz[1][j]

print('=' * 30)

print(f'Soma dos números pares na matriz: {sTotal}')
print(f'Soma dos valores da terceira coluna: {sTC}')
print(f'Maior valor da segunda linha: {maiorValorSL}')
