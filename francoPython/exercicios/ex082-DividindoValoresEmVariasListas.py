lista1 = []
listaPar = []
listaImpar = []

while True:

    num = int(input('Digite um número qualquer: '))
    lista1.append(num)

    continuar = input('Deseja continuar incluindo números? (S/N): ').strip()[0]

    while continuar not in 'sSnN':
        continuar = input('Opção inválida. Deseja continuar incluindo números? (S/N): ').strip()[0]

    if continuar in 'nN':
        break

for n in lista1:
    if n % 2 == 0:
        listaPar.append(n)

    else:
        listaImpar.append(n)

print('=' * 30)
print(f'Lista principal: {lista1}')
print(f'Lista de valores pares: {listaPar}')
print(f'Lista de valores ímpares: {listaImpar}')
print('=' * 30)
