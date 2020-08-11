continuar = 's'

maior = homens = mulherm20 = 0

while True:

    while continuar == 's':

        print('-' * 30)
        sexo = input('Informe o sexo correspondente: ').strip()

        while sexo not in 'MFmf':
            sexo = input('Informe o sexo correspondente: ').strip()

        idade = int(input('Informe a idade correspondente: '))
        print('-' * 30)

        if idade >= 18:
            maior += 1

        if sexo in 'Mm':
            homens += 1

        if idade < 20 and sexo in 'Ff':
            mulherm20 += 1

        continuar = input('\nDeseja cadastrar mais informações pesoais? (s/n): ').strip().lower()[0]

        while continuar not in 'simnaosn':
            continuar = input('\nDeseja cadastrar mais informações pesoais? (s/n): ').strip().lower()[0]

    print('\nInformações cadastradas!\n')
    break

print('======= Relatório =======\n')
print(f'Número de pessoas maiores de 18 anos: {maior}')
print(f'Número de homens: {homens}')
print(f'Número de mulheres menores de 20 anos: {mulherm20}\n')
print('=' * 26)
