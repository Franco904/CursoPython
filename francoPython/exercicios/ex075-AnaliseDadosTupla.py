tNum = (int(input('Informe um número: ')),
        int(input('Informe outro número: ')),
        int(input('Informe outro número: ')),
        int(input('Informe mais outro número: ')))

print(f'O número 9 apareceu {tNum.count(9)} vezes na tupla de números informados.')

if 3 in tNum:
    print(f'O número 3 apareceu na {tNum.index(3) + 1}ª posição da tupla de números informados.')

else:
    print('O valor 3 não foi encontrado na tupla de números informados.')

print(f'Os números pares são: ', end='')
for n in tNum:

    if n % 2 == 0:
        print(n, end=' ')



