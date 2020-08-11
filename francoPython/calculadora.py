nome = input('Olá desenvolvedor! Qual o seu nome? ')
print('É um prazer conhecê-lo', nome, ', queira conhecer a minha mais nova calculadora:\n')
continuar = 'sim'

while  continuar == 'sim':

    escolha = input('Digite um caracter de operação (+, -, * ou /) para o cálculo: ')

    if escolha != '+' and escolha != '-' and escolha != '*' and escolha != '/':
        print('Selecione um operador válido!')

    else:

        num1 = int(input('Digite aqui o primeiro número: '))
        num2 = int(input('Agora digite aqui o segundo número: '))

        if escolha == '+':
            soma = num1 + num2
            print(f'A soma de {num1} e {num2} é {soma}')

        elif escolha == '-':
            subtracao = num1 - num2
            print(f'A subtração de {num1} e {num2} é {subtracao}')

        elif escolha == '*':
            multiplicacao = num1 * num2
            print(f'A multiplicação de {num1} e {num2} é {multiplicacao}')

        elif escolha == '/':
            divisao = num1 * num2
            print(f'A divisão de {num1} e {num2} é {divisao}')

        gostou = input('Gostou? ')

        if gostou.__eq__('sim'):
            print('Eu sabia que você iria gostar :)')

        elif gostou.__eq__('nao'):
            print('É uma pena, vou tentar melhorá-la prontamente! :)')

        continuar = input('Deseja continuar calculando? ')

print('Hora de dormir...')