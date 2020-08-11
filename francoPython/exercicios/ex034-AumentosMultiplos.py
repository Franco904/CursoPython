sal = float(input('Informe o seu salário atual: '))

if sal <= 0:
    print('Impossível obter salários menores ou iguais a R$ 0,00!')

elif sal <= 1250:

    aum = sal + (sal * 0.15)
    print(f'Seu salário com aumento foi de {aum}!')

else:

    aum = sal + (sal * 0.1)
    print(f'Seu salário com aumento foi de {aum}!')