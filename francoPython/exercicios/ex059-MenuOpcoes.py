from time import sleep

print('Calculadora\n')

x = int(input('Digite um número qualquer: '))
y = int(input('Digite outro número: '))

maior = x

print('\nMenu de operações:\n')
print('[ 1 ] - Soma')
print('[ 2 ] - Multiplicação')
print('[ 3 ] - Maior dos números')
print('[ 4 ] - Digitar outros números')
print('[ 5 ] - Sair da Calculadora')

opcao = 0

while opcao != 5:

    opcao = int(input('\nDigite uma das opções no menu: '))

    if opcao == 1:
        print(f'\nA soma entre {x} e {y} é {x + y}')

    elif opcao == 2:
        print(f'\nA multiplicação entre {x} e {y} é {x * y}')

    elif opcao == 3:
        if y > x:
            print(f'{y} é o maior número')

        else:
            print(f'{x} é o maior número')

    elif opcao == 4:
        print('\nInforme novamente os números:')

        x = int(input('Digite um número qualquer: '))
        y = int(input('Digite outro número: '))

    elif opcao == 5:
        print('\nFechando o programa...')

    else:
        print('Opção inválida.')

sleep(1)
print('\nCalculadora OFF')
