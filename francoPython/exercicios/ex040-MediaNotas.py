nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Aluno aprovado.')

elif media >= 5 and media < 7:
    print('Aluno sujeito a recuperação.')

else:
    print('Aluno reprovado.')
