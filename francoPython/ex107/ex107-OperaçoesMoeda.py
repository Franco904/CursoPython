from ex107 import moeda

p = float(input('Digite o preço: R$ '))

print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13%, temos R$ {moeda.diminuir(p, 13)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}')