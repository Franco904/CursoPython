def quebra():
    print('\n')

def lin():
    print('=' * 30)


def tit(txt):
    print('=' * 35)
    print(txt)
    print('=' * 35)

#
# # Programa Principal
#
# tit(f'{"    Aula de Funções em Python   ":^35}')
# tit(f'{"    Franco Saravia Tavares   ":^35}')
# tit(f'{"    03/04/2020   ":^35}')
#
# lin()

def soma(a, b):
    print(f'A = {a} e B = {b}')
    print(f'A soma de A + B vale {a + b}')
    print('\n')

# Programa Principal


soma(b = 4, a = 5)
soma(8, 9)
soma(2, 1)


def contador(* num):
    for i, v in enumerate(num):
        print(f'Na posição {i + 1} há o valor {v}')
    quebra()
    tam = len(num)
    print(f'Recebi os valores {num} que ao todo são {tam}')


contador(4, 6, 7)
contador(6, 7, 4, 3, 1)
contador(2, 9, 10, 12)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(f'Lista com valores dobrados: {lst}')

lista = list()

for i in range(0, 5):
    lista.append(int(input('Qual item deseja adicionar a lista? ')))

print(f'Lista com os valores adicionados: {lista}')
dobra(lista)
