import random

tNum = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

print(f'\nEstes são os números gerados na lista: ', end='')

for num in tNum:
    print(f'{num} ', end='')

print('\n')
print('-' * 30)
print(f'O maior valor na tupla é {max(tNum)}')
print('-' * 30)
print(f'O menor valor na tupla é {min(tNum)}')
print('-' * 30)

