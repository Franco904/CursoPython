import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.pow(co, 2) + math.pow(ca, 2)

print(f'A valor da hipotenusa resultante dos catetos {co} e {ca} é de {math.sqrt(h)}')