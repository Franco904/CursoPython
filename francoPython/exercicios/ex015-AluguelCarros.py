km = float(input('Informe a quantidade de quilometros rodados pelo carro: '))
dias = int(input('Informe o número de dias pelo qual o carro foi alugado: '))

preco_km = km * 0.15
preco_dias = dias * 60
mont = preco_km + preco_dias

print(f'O montante a pagar pelo carro alugado será de R$ {mont}')