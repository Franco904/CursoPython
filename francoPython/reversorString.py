def lin():
    print('=' * 30)

lin()
txt = str(input('Digite um texto: ')).strip()
lin()
reverso = ''

for i in range(len(txt) - 1, -1, -1):
    reverso += txt[i]

print(f'Texto revertido: {reverso}')
lin()