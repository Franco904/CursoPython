num = soma = dig = 0

num = int(input('Digite um número qualquer (999 para parar): '))

while True:

    if num != 999:
        soma += num

    else:
        break

    num = int(input('Digite um número qualquer (999 para parar): '))

    dig += 1

print(f'A soma dos {dig} números digitados foi de {soma}.')
