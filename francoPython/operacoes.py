def mensagem(msg):
    print('=' * 30)
    print(msg)


def fatorial(num):

    f = 1

    for i in range(num, 1, -1):

        f *= i
        i += 1

    return f


print('=' * 30)
num1 = int(input('Digite um número qualquer: '))
num2 = int(input('Digite um segundo número: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisaoInteira = num1 // num2
potencia = num1 ** num2

mensagem(f'Soma = {soma}')
mensagem(f'Subtração = {subtracao}')
mensagem(f'Multiplicação = {multiplicacao}')
mensagem(f'Divisão = {divisao:.2f}')
mensagem(f'Divisão Inteira = {divisaoInteira}')
mensagem(f'Potência = {potencia:.2f}')

mensagem(f'Fatorial de {num1} é {fatorial(num1)}')
mensagem(f'Fatorial de {num2} é {fatorial(num2)}')
print('=' * 30)