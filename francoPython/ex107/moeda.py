def aumentar(preco, aumento):

    res = preco * (1 + aumento/100)
    return res


def diminuir(preco, diminuiçao):

    res = preco * (1 - diminuiçao/100)
    return res


def dobro(preco):

    res = preco * 2
    return res


def metade(preco):

    res = preco / 2
    return res
