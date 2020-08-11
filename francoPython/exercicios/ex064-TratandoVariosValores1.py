num = 0
soma = 0
dig = 0

while num != 999:

    num = int(input('Digite um número qualquer (999 para parar): '))

    if num != 999:
        soma += num

    dig += 1

print(f'A soma dos {dig - 1} números digitados foi de {soma}')
