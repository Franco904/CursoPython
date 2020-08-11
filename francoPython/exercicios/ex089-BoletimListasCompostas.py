ficha = list()
continuar = 's'

while continuar in 'sSsimSIM':
    nome = input('Informe o nome do aluno: ').title().strip()
    nota1 = float(input('Informe a primeira nota do aluno: '))
    nota2 = float(input('Informe a segunda nota do aluno: '))

    m = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], m])

    continuar = input('Quer continuar incluindo dados? (S/N): ').strip()

    while continuar not in 'sSnNsimSIMnaoNAO':
        continuar = input('Quer continuar incluindo dados? (S/N): ').strip()

print('=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('=' * 30)

for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

print('=' * 30)

while True:

    print('=' * 30)
    o = int(input('Deseja mostrar as notas de qual aluno? (999 para interromper) '))

    if o == 999:
        print('Encerrando o programa...')
        break

    if o <= len(ficha) - 1:
        print(f'Notas de {ficha[o][0]} são {ficha[o][1]}')

print()