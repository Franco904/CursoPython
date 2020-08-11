print('Este é um menu de conversões de números! Opções:\n')
print('[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal\n')
opcao = input('Digite uma opção para conversão: ')

if opcao == '1':
    num = int(input('Informe um número a converter para binário: '))
    print(f'{num} em binário é {bin(num)[2:]}')

elif opcao == '2':
    num = int(input('Informe um número a converter para octal: '))
    print(f'{num} em octal é {oct(num)[2:]}')

elif opcao == '3':
    num = int(input('Informe um número a converter para hexadecimal: '))
    print(f'{num} em hexadecimal é {hex(num)[2:]}')

else:
    print('Opção inválida!')
