from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'franco.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    try:
        menu()
        op = int(input('Opção: '))

    except ValueError:
        print('\033[31mErro ao inserir o dado!\033[m')

    else:
        if op == 1: # Listar conteúdo do arquivo!
            lerArquivo(arq)

        elif op == 2: # Criar um novo cadastro!
            cabeçalho('NOVO CADASTRO'.center(40))
            nome = input('Nome: ').title().strip()
            idade = leiaInt('Idade: ')

            cadastrar(arq, nome, idade)

        elif op == 3: # Fechar programa.
            cabeçalho('-- PROGRAMA ENCERRADO --'.center(40))

            break

        else:
            cabeçalho('\033[31mOPÇÃO INVÁLIDA!\033[m'.center(50))

        sleep(2)




