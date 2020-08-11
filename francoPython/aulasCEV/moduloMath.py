from math import sqrt, ceil, floor  ## ou 'import math'

num = int(input('Digite um número: '))
raiz = sqrt(num)

print(f'a raiz de {num} é {raiz}')
print(f'a raiz de {num} arrendondando para cima é {ceil(raiz)}')
print(f'a raiz de {num} arrendondando para baixo é {floor(raiz)}')