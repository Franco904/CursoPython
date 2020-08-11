num1 = input('Digite um valor para o primeiro número: ')
num2 = input('Digite um valor para o segundo número: ')

if num1 > num2:
    print(f'O primeiro valor ({num1}) é maior que o segundo ({num2}).')

elif num2 > num1:
    print(f'O segundo valor ({num2}) é maior que o primeiro ({num1}).')

else:
    print(f'Os números são iguais.')