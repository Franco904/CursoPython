livros = dict()

livros['nome do livro'] = 'Inferno'
livros['ano'] = '2013'
livros['diretor'] = 'Dan Brown'

print(livros.values())
print(livros.keys())
print(livros.items(), '\n')

for k, v in livros.items():
    print(f'O {k} é {v}')

print('=' * 30)

pessoas = {'nome': 'Franco', 'sexo': 'M', 'idade': 16}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')

del pessoas['sexo']
pessoas['nome'] = 'Augusto'
pessoas['idade'] = 14
pessoas['peso'] = 50

print('\nValores: ')
for v in pessoas.values():
    print(v)

print('=' * 30)

# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
# estado3 = {'uf': 'São Paulo', 'sigla': 'SP'}
#
# brasil = list()
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(brasil[1]['uf'])

estado = dict()
brasil = list()

for i in range(0, 3):

    estado['uf'] = input('Unidade Federativa: ').title()
    estado['sigla'] = input('Sigla do Estado: ').upper()
    brasil.append(estado.copy())

print('\n')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()



