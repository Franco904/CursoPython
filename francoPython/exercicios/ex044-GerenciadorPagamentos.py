print('Olá cliente! Veja as opções de como efetuar seu pagamento:\n')

print('[ 1 ] À vista em dinheiro/cheque (desconto de 10% na compra)')
print('[ 2 ] À vista no cartão (desconto de 5% na compra)')
print('[ 3 ] Em até 2x no cartão (preço normal)')
print('[ 4 ] 3x ou mais no cartão (juros de 20% na compra)\n')

opcao = int(input('Qual opção deseja escolher? '))
preco = float(input('Informe o preço do produto para a compra: '))

desconto10 = preco - (preco * 0.1)
desconto5 = preco - (preco * 0.05)
juros20 = preco + (preco * 0.2)

if opcao == 1:
    print(f'O preço total com desconto de 10% foi de R$ {desconto10}')

elif opcao == 2:
    print(f'O preço total com desconto de 5% foi de R$ {desconto5}')

elif opcao == 3:
    print(f'O preço total foi de R$ {preco}')

elif opcao == 4:
    print(f'O preço total com juros de 20% foi de R$ {juros20}')

else:
    print('Opção inválida!')