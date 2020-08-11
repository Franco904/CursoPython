def tit():
    print('===== Controle de Terrenos =====\n')


def area(b, h):
    a = b * h
    print(f'A área do auperfície retangular {b} x {h} é {a} m²')


# Programa principal

tit()

base = float(input('Digite a base do retângulo em metros: '))
altura = float(input('Digite a altura do retângulo em metros: '))

area(base, altura)
