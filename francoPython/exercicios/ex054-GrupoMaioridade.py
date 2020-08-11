maior = 0

for i in range(1, 8):
    ano = int(input(f'Informe o ano de nascimento da {i}° pessoa: '))
    dif = 2020 - ano

    if dif >= 18:
        maior += 1

print(f'\n{maior} pessoas já atingiram a maioridade e {7 - maior} ainda não a atingiram.')
