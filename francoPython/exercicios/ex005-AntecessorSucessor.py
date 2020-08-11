num = int(input('Digite um número qualquer: '))

print(f'Número informado: \033[1;35m{num}\033[m')
print(f'\033[4;36mAntecessor\033[m: \033[1;35m{num - 1}\033[m')
print(f'\033[4;36mSucessor\033[m: \033[1;35m{num + 1}\033[m')