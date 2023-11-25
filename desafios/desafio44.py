preco = float(input('Valor do produto: R$'))
print('''------------------------------
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão
------------------------------''')
escolha = int(input('Escolha: '))
if escolha == 1:
    novo_preco = preco - (preco * 10 / 100)
elif escolha == 2:
    novo_preco = preco - (preco * 5 / 100)
elif escolha == 3:
    novo_preco = preco
else:
    parcelas = int(input('Quantas parcelas? '))
    novo_preco = preco + (preco * 20 / 100)
    parceladas = novo_preco / parcelas
    print(f'\nSua compra será parcelada em {parcelas}x de R${parceladas:.2f} com JUROS')
print(f'Considerando a condição de pagamento, o produto custa agora R${novo_preco:.2f}')