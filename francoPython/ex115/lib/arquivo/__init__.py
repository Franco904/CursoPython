from ex115.lib.interface import *

def arquivoExiste(arq):
    try:
        a = open(arq, 'rt') # "Read Text"
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        a = open(arq, 'wt+') # "Write Text". '+' Cria (write) caso o arquivo não exista.
        a.close()
    except:
        print('\033[31mErro ao criar o arquivo!\033[m')
    else:
        print(f'-> Arquivo {arq} criado com sucesso!')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS'.center(40))
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()


def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at') # "Append Text". Insere um novo valor à lista criada.
    except:
        print('\033[31mErro ao abrir o arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mErro ao escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
