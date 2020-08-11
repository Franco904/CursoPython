import math

ang = int(input('Digite um ângulo qualquer: '))

sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'Os valores do seno, cosseno e tangente de {ang}° são, respectivamente, {sin:.2f}, {cos:.2f} e {tan:.2f}')