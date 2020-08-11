def cont(i, f, p):
    """
    -> Faz contagem de números
    :param i: ponto de início
    :param f: ponto final
    :param p: Passo (razão da sequência)
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(c, sep='-', end=' ')
        c += p
    print('Fim')
# cont(2, 10, 2)

# help(cont) # Interactive Help


def soma(a=0, b=0, c=0): # Parâmetros (args) opcionais
    """
    -> Faz a soma dos fatores informados
    :param a: Primeiro fator
    :param b: Segundo fator
    :param c: Terceiro fator
    :return: Sem retorno
    """
    s = a + b + c
    print(f'Soma: {s}')

# soma(3, 2, 5)
# soma(8, 4)

def teste(b):

    # Dentro da função (método), chamamos o escopo de LOCAL
    global a
    a = 8
    b += 4
    c = 2
    print(f'"A" local vale {a}')
    print(f'"B" local vale {b}')
    print(f'"C" local vale {c}')


# Fora da função (método), chamamos o escopo de GLOBAL
# a = 5
# teste(a)
# print(f'"A" global vale {a}')


def soma(a=0, b=0, c=0):

    s = a + b + c
    return s


# r1 = soma(3, 2, 5)
# r2 = soma(8, 4)
#
# print(f'As somas valem respectivamente {r1} e {r2}')

def fatorial(num = 1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f


# n = int(input('Digite um número: '))
# facn = fatorial(n)
# print(f'O fatorial de {n} é {facn}')
#
# r1 = fatorial(5)
# r2 = fatorial(4)
# r3 = fatorial() # Insere o argumento reserva (num=1) quando nada é indicado
#
# print(f'Os resultados são {r1}, {r2} e {r3}')

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

numero = int(input('Número: '))

if par(numero):
    print(f'{numero} é par!')

else:
    print(f'{numero} é ímpar!')


