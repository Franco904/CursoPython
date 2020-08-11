s = 0
maisVelho = 0
mulherMenor20 = 0
nomeMaisVelho = ''

for i in range(1, 5):

    nome = input(f'\nInforme o nome da {i}ª pessoa: ').strip().title()
    idade = int(input(f'Informe a idade da {i}ª pessoa: '))
    sexo = input(f'Informe o sexo (M ou F) da {i}ª pessoa: ').strip().upper()

    s += idade

    if sexo == 'M':

        if idade > maisVelho:
            maisVelho = idade
            nomeMaisVelho = nome

    if sexo == 'F':

        if idade < 20:
            mulherMenor20 += 1

m = s/i

print('\n\nRelatório:')

print(f'\nA média de idade do grupo é de {m} anos')
print(f'O homem mais velho tem {maisVelho} anos e se chama {nomeMaisVelho}')

if mulherMenor20 != 0:
    print(f'Há {mulherMenor20} mulheres com menos de 20 anos.')

else:
    print('Não há mulheres com menos de 20 anos.')