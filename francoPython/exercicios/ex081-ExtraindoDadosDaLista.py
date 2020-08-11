lista = []
continuar = 's'
qNum = 0

while True:

    lista.append(int(input('Digite um número qualquer: ')))
    qNum += 1

    continuar = input('Deseja continuar incluindo números? (S/N): ').strip()[0]

    while continuar not in 'sSnN':
        continuar = input('Opção inválida. Deseja continuar incluindo números? (S/N): ').strip()[0]

    if continuar in 'nN':
        break

print('=' * 30)

print(f'Foram lidos {qNum} números')
print(f'Estes são os valores ordenados de forma descrescente: {sorted(lista, reverse=True)}')

if 5 in lista:
    print('O número 5 faz parte da lista de valores informados.')

else:
    print('O número 5 não foi informado.')


