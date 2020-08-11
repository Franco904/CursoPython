idadeComp = int(input('Informe a idade do competidor: '))

if idadeComp <= 9 and idadeComp >= 0:
    print('Categoria do competidor: MIRIM')

elif idadeComp > 9 and idadeComp <= 14:
    print('Categoria do competidor: INFANTIL')

elif idadeComp > 14 and idadeComp <= 19:
    print('Categoria do competidor: JUNIOR')

elif idadeComp > 19 and idadeComp <= 20:
    print('Categoria do competidor: SÊNIOR')

elif idadeComp > 20:
    print('Categoria do competidor: MASTER')

else:
    print('A idade informada é inválida!')