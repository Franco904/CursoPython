import random

a1 = input('Informe o nome de um aluno na sala: ')
a2 = input('Informe o nome de outro aluno: ')
a3 = input('Informe o nome de mais outro aluno na sala: ')
a4 = input('Informe o nome de mais outro aluno: ')

listaAlunos = [a1, a2, a3, a4]
random.shuffle(listaAlunos)

print(f'Professor, a ordem dos alunos sorteada para apresentar os trabalhos foi:')
print(listaAlunos)