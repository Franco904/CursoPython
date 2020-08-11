dados = dict()

aluno = input('Qual o nome do aluno? ').title().strip()
media = float(input(f'Qual foi a média de {aluno}? '))

dados['nome'] = aluno
dados['media'] = media

print('=' * 30)
print(f'Nome do aluno: {dados["nome"]}')
print(f'Média: {dados["media"]}')

if media >= 7:
    dados['situacao'] = 'Aprovado'
    print(f'Situação - {dados["situacao"]}')

elif media >= 0 and media < 7:
    dados['situacao'] = 'Reprovado'
    print(f'Situação - {dados["situacao"]}')

else:
    print('Impossível haver média negativa!')


