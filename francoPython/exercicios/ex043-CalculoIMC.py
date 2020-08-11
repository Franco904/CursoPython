from math import pow

peso = float(input('Informe o seu peso em quilogramas: '))
altura = float(input('Informe a sua altura em metros: '))

imc = peso / pow(altura, 2)

print('\n')

if imc < 18.5:
    print(f'IMC ({imc:.1f}): Abaixo do peso')

elif imc >= 18.5 and imc < 25:
    print(f'IMC ({imc:.1f}): Peso ideal')

elif imc >= 25 and imc < 30:
    print(f'IMC ({imc:.1f}): Sobrepeso')

elif imc >= 30 and imc < 40:
    print(f'IMC ({imc:.1f}): Obesidade')

else:
    print(f'IMC ({imc:.1f}): Obesidade mórbida')