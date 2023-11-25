preco = float(input('Preço do produto: R$'))
novo_preco = preco - (preco * 5 / 100)
print(f'O produto que custava R${preco:.2f} passou a custar R${novo_preco:.2f}')
