galera = list()
dado = list()
totmaior = totmenor = 0

for i in range(1, 6):

    dado.append(input(f'{i}º Nome: ').title().strip())
    dado.append(int(input(f'{i}ª Idade: ')))

    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        totmaior += 1

    else:
        print(f'{p[0]} é menor de idade!')
        totmenor += 1

print(f'\nO total de maiores de idade é: {totmaior}')
print(f'O total de menores de idade é: {totmenor}')