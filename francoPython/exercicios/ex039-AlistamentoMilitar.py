idade = int(input('Qual a sua idade? '))

if idade == 18:
    print('Está na hora de você se alistar!')

elif idade > 18:
    print(f'Você já passou {idade - 18} anos do prazo de alistamento!')

elif idade >= 0 and idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você poder se alistar!')

else:
    print('Idade inválida!')
