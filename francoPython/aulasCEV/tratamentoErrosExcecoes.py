try:
    x = int(input('Número 1: '))
    y = int(input('Número 2: '))
    d = x/y

# except Exception as erro:
#     print(f'Erro! {erro.__class__}')

except KeyboardInterrupt:
    print('Número não informado.')

except (ValueError, TypeError):
    print('Erro! Tipo de dado incorreto!')

except ZeroDivisionError:
    print('Erro! Impossível dividir por zero!')

else:
    print(f'Divisão: {d:.1f}')

finally:
    print('Volte sempre!')
