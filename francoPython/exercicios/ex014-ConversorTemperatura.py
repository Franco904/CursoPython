escolha = input('Escolha uma escala termométrica para realizar a conversão (c, f ou k): ')

if escolha.lower() == 'c':

    c = float(input('Informe um valor em Celsius: '))

    f = ((9 * c) / 5 + 32)
    k = c + 273

    print(f'{c}°C equivalem a {f}°F')
    print(f'{c}°C equivalem a {k}K')

elif escolha.lower() == 'f':

    f = float(input('Informe um valor em Fahrenheit: '))

    c = (5 * f - 160) / 9
    k = (5 * f - 160) / 9 + 273

    print(f'{f}°F equivalem a {c}°C')
    print(f'{f}°F equivalem a {k}K')

elif escolha.lower() == 'k':

    k = float(input('Informe um valor em Kelvin: '))

    c = k - 273
    f = (9 * (k - 273)) / 5 + 32

    print(f'{k}K equivalem a {c}°C')
    print(f'{k}K equivalem a {f}°F')

else:

    print('Escolha inválida!')