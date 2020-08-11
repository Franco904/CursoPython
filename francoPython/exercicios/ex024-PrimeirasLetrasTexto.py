cidade = input('Informe o nome de uma cidade: ').strip()

if cidade[:5].title() == 'Santo':

    print(f'{cidade} tem "Santo" no primeiro nome!')

else:

    print(f'{cidade} não tem "Santo" no primeiro nome!')