print(f'{" LOJAS BENTO ":=^30}')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista de dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    novo_preco = preco - (preco * 10 / 100)
elif opcao == 2:
    novo_preco = preco - (preco * 5 / 100)
elif opcao == 3:
    novo_preco = preco
    parceladas = novo_preco / 2
    print(f'Sua compra será parcelada em 2x de R${parceladas:.2f} SEM JUROS')
elif opcao == 4:
    novo_preco = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    parceladas = novo_preco / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${parceladas:.2f} COM JUROS')
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
    novo_preco = preco
print(f'Sua compra de R${preco:.2f} vai custar R${novo_preco:.2f} no final.')
