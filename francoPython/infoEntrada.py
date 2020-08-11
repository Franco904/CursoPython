entrada = input('Digite algo: ')
print(type(entrada))

if entrada.isspace():
    print(f'"{entrada}" é um espaço em branco')

if entrada.isalpha():
    print(f'{entrada} é alfabético')

if entrada.isnumeric():
    print(f'{entrada} é númerico')

if entrada.isalnum():
    print(f'{entrada} é alfanumérico')

if entrada.islower():
    print(f'{entrada} está em minúsculo')

if entrada.isupper():
    print(f'{entrada} está em maiúsculo')

if entrada.isdigit():
    print(f'{entrada} é um dígito')

else:
    print(f'{entrada} não é um dígito')

if entrada.isdecimal():
    print(f'{entrada} é um número decimal')

else:
    print(f'{entrada} não é um número decimal')

if entrada.isidentifier():
    print(f'{entrada} é um identificador válido')

else:
    print(f'{entrada} não é um identificador válido')

if entrada.isprintable():
    print(f'{entrada} é próprio para impressão')

else:
    print(f'{entrada} não é próprio para impressão')

if entrada.istitle():
    print(f'{entrada} está capitalizada')

else:
    print(f'{entrada} não está capitalizada')