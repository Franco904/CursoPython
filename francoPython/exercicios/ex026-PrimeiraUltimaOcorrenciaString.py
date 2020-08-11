frase = input('Digite uma frase qualquer: ').lower()

letrasA = frase.count('a')
primeiroA = frase.find('a')
ultimoA = frase.rfind('a')

print(f'\nNúmero de "A"s na frase: {letrasA}')
print(f'Primeiro "A": {primeiroA + 1}° posição')
print(f'Último "A": {ultimoA + 1}° posição')
