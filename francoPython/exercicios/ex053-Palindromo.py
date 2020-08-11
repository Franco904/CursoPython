frase = input('Digite uma frase: ').strip().upper()

p = frase.split()
juncao = ''.join(p)
inverso = ''

for letra in range(len(juncao) - 1, -1, -1):
    inverso = inverso + juncao[letra]

print(f'O inverso de {juncao} é {inverso}')

if juncao == inverso:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')