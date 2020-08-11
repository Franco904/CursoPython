d = float(input('Indique a distância em Km percorrida na viagem: '))

if d < 0:
    print('Impossível percorrer distâncias negativas!')

elif d >= 0 and d <= 200:

    vPassagem = d * 0.5
    print(f'O valor da passagem para {d} km é de R${vPassagem}')

elif d > 200:

    vPassagem = d * 0.45
    print(f'O valor da passagem para {d} km é de R${vPassagem}')