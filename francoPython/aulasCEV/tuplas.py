lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Chips')
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[-1])
print(lanche[-2])
print(lanche[1:])
print(lanche[:2])
print(lanche[-2:])

# AS TUPLAS SAO IMUTÁVEIS:

# lanche[1] = 'Sorvete'
# print([1])

print('\n')

for comida in lanche:    # For comida dentro de lanche:
    print(f'Eu vou comer {comida}')

# ou:
print('\n')

for i in range(0, len(lanche)):    # For contador entre o tamanho da tupla lanche:
    print(f'Eu vou comer {lanche[i]}')

print('\n')

for p, comida in enumerate(lanche): # For comida e posição da comida dentro da tupla lanche
    print(f'Eu vou comer {comida} na posição {p}')

print(sorted(lanche)) # Tupla mostrada em ordem alfabética

print('Vou comer à beça!')

print('\n')

print('Tupla A: ')
a = (1, 2, 10, 10, 5)
print(a)

print('\nTupla B: ')
b = (10, 11, 12, 13, 14)
print(b)

print('\nTupla C (soma de a + b): ')
c = a + b
print(c)

print(f'\nA tupla C possui {len(c)} elementos')
print(f'Na tupla C existem {c.count(10)} números 10')
print(f'O número 14 está na {c.index(14) + 1}ª posição da tupla C')
print(f'O número 10 está na {c.index(10, 4) + 1}ª posição da tupla C') # Procurar ocorrencias do numero 10 depois da posição 4

del(c) # Exclui a tupla c