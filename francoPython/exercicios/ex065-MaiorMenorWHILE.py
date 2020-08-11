continuar = 'S'

media = i = maior = menor = 0

while continuar == 'S':

    num = int(input('Informe um número: '))

    media += num
    i += 1

    if i == 1:
        maior = menor = num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    continuar = input('Deseja continuar digitando números? ').upper().strip()[0]

media = media / i
print(f'\nA média dos números é de {media}')

print(f'\nO maior valor lido foi {maior} e o menor foi {menor}.')