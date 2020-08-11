valorCasa = int(input('Informe o valor da casa: '))
sal = int(input('Informe o salário do comprador: '))
anos = int(input('Informe em quantos anos a pessoa vai comprar a casa: '))

presMensal = valorCasa / (anos * 12)
min = sal * 0.3

if presMensal <= min:
    print(f'Empréstimo aprovado! Com R$ {presMensal:.2f} você está apto para comprar a casa.')

else:
    print(f'Empréstimo negado! Com R$ {presMensal:.2f} você não está apto ainda para comprar a casa.')


