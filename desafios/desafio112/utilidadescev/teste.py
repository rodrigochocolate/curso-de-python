from desafios.desafio112.utilidadescev import dado, moeda

p = dado.leiaDinheiro('Digite o preço: R$')
print(moeda.aumentar(p, 10, True))
