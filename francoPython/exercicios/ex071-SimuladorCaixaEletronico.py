v = int(input('Informe o valor a ser sacado: R$'))

total = v
tCed = 0
ced = 50

while True:

    if total >= ced: # se o valor a sacar for maior do que uma nota de 50 (possibilidade de sacar)
        total -= ced # tirar cinquenta reais quantas vezes conseguir
        tCed += 1  # numero de notas de cinquenta sacadas

    else:
        if tCed > 0:
            print(f'Total de {tCed} cédulas de {ced} reais')

        if ced == 50:
            ced = 20

        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 1

        tCed = 0 # ao mudar a cédula, o total destas zera novamente

        if total == 0: # se nao houver como pagar
            break

print('\nVolte sempre! Tenha um bom dia!')

