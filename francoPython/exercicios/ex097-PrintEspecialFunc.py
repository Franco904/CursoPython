def escreva(msg):
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)


# Programa principal

mensagem = input(f'Mensagem: ').strip()
escreva(mensagem)
print('\nFim')