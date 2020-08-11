continuar = 's'

totalPreco = acimaMil = i = 0
precoB = 100000000
nomeB = ''

while True:

    while continuar == 's':

        print('-' * 30)
        nome = input('Informe o nome do produto para a compra: ').strip()
        preco = float(input('Informe o preço do produto correspondente: '))
        print('-' * 30)

        totalPreco += preco

        if preco > 1000:
            acimaMil += 1

        if preco < precoB:
            precoB = preco
            nomeB = nome

        continuar = input('Deseja cadastrar mais produtos? (s/n): ').strip().lower()[0]

        while continuar not in 'simnaosn':
            continuar = input('Deseja cadastrar mais produtos? (s/n): ').strip().lower()[0]

    print('\nProdutos cadastrados!\n')
    break

print('======= Informações de compra =======\n')
print(f'Preço total: R${totalPreco}')
print(f'Quantidade de produtos com preço acima de R$1000,00: {acimaMil}')
print(f'Produto mais barato comprado: {nomeB} (R${precoB})\n')
print('=' * 40)
