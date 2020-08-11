matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor na posição [{i}, {j}]: '))

print('=' * 30)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]:^5} ]', end='')
    print()
