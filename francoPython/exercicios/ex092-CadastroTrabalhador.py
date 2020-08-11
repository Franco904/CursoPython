from datetime import date
from time import sleep

dados = dict()

dados['nome'] = input('Nome: ').strip().title()

anoNasc = int(input('Ano de nascimento: '))

idade = date.today().year - anoNasc

dados['idade'] = idade
dados['ct'] = int(input('Carteira de trabalho (0 - Não tem): '))

if dados['ct'] != 0:

    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário atual: R$ '))

    dados['idadeApos'] = (dados['contratacao'] + 35) - anoNasc

    print('\n== DADOS CONCLUÍDOS ==\n')
    sleep(1)
    print(f'Nome: {dados["nome"]}')
    sleep(1)
    print(f'Idade: {dados["idade"]}')
    sleep(1)
    print(f'Carteira de Trabalho: {dados["ct"]}')
    sleep(1)
    print(f'Ano de contratação: {dados["contratacao"]}')
    sleep(1)
    print(f'Salário correspondente: {dados["salario"]}')
    sleep(1)
    print(f'Idade em que vai aposentar-se: {dados["idadeApos"]} anos')

    print('=' * 30)

else:

    print('\n== DADOS CONCLUÍDOS ==\n')
    sleep(1)
    print(f'Nome: {dados["nome"]}')
    sleep(1)
    print(f'Idade: {dados["idade"]}')
    sleep(1)
    print(f'Carteira de Trabalho: {dados["ct"]}')

    print('=' * 30)
