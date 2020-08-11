vel = int(input('Informe a velocidade atual do carro: '))

velExc = vel - 80

if vel > 80:
    multa = velExc * 7

    print(f'Você receberá R${multa},00 de multa por dirigir acima de 80 km/h!')

print(f'Você não receberá nenhuma multa.')