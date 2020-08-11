nome = input('Digite o seu nome completo: ').strip()

maiuscula = nome.upper()
minuscula = nome.lower()
dividido = nome.split()

print(f'\nNome com todas as letras maiúsculas: {maiuscula}')
print(f'\nNome com todas as letras minúsculas: {minuscula}')
print(f'\nNúmero de caracteres no nome: {len(nome) - nome.count(" ")}')
print(f'\nNúmero de caracteres no primeiro nome: {len(dividido[0])}')