sexo = input('Informe seu sexo (M ou F): ').strip().upper()

while sexo not in 'MF':
    sexo = input('Sexo inválido. Digite seu sexo: ')


if sexo == 'M':
    print('Sexo registrado como homem.')

elif sexo == 'F':
    print('Sexo registrado como mulher.')