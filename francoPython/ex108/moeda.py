def aumentar(preco=0, aumento=0):

    res = preco * (1 + aumento/100)
    return res


def diminuir(preco=0, diminuiçao=0):

    res = preco * (1 - diminuiçao/100)
    return res


def dobro(preco=0):

    res = preco * 2
    return res


def metade(preco=0):

    res = preco / 2
    return res


def moeda(preco=0, moeda='R$ '):

    return f'{moeda}{preco:.2f}'.replace('.', ',')
