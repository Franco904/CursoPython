m = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(0, 4):
    for j in range(0, 4):
        m[i][j] = input(f'Digite um valor na posição [{i}, {j}]: ')

print('=' * 30)
print('MATRIZ'.center(30))
print('=' * 30)

for i in range(0, 4):
    for j in range(0, 4):
        print(f'[{m[i][j]}]'.center(5), end=' ')
    print()