bairros = ['itacorubi', 'trindade', 'santa monica', 'pantanal', 'agronomica', 'centro', 'canasvieiras']

# LISTAS SÃO MUTÁVEIS

del bairros[4]  # Elimina a string da posicão 4 da lista
bairros.pop(2)  # Também elimina a string na posição 2 da lista
bairros.remove('pantanal')  # Elimina string da lista pelo nome correspondente

bairros.pop()   # Elimina o último elemento da lista somente

if 'pantanal' in bairros:   # Se pantanal estiver na lista de bairros, elmine-o
    bairros.remove('pantanal')

print(bairros)

bairros.insert(7, 'coqueiros') # Adicionar novo valor à lista na posição 7

print(bairros)

print('=' * 30)

numeros = list(range(1, 6))     # Lista com 5 números

print(numeros)

valores = [8, 7, 1, -1, 2, 4, 6]    # Lista com números desordenados
valores.sort()      # Ordenar a lista em ordem crescente

print(valores)

valores.sort(reverse=True)      # Ordenar a lista em ordem decrescente

print(valores)
print(len(valores))    # Mostra quantos elementos há na lista

valores.append(11) # Adiciona o número 11 à última posição da lista
print(valores)

print('=' * 30)

numeros = []
numeros.append(2)
numeros.append(5)
numeros.append(8)

for n in numeros:
    print(n, end=' ')

print('\n')

for i in range(0, 5):   # Adicionar números pelo teclado a lista de números pre-existentes

    numeros.append(int(input('Digite um número: ')))

for i, n in enumerate(numeros):
    print(f'Na posição {i} encontrei o número {n}.')
print('Cheguei ao final da lista!')

print(f'\nLista de números: {numeros}')

print('=' * 30)

a = [0, 1, 2, 3]
b = a[:]    # Copia os valores de a para b (sem fazer ligação)
b[2] = 9

print(f'Lista A: {a}')
print(f'Lista B: {b}')