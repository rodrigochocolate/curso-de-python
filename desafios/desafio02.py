from time import sleep

cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'magenta': '\033[35m',
         'verde': '\033[32m',
         'amarelo': '\033[0;33m',
         'branco': '\033[0;30m',
         'vermelho': '\033[31m',
         'vermelho1': '\033[1;31m'}

dia = int(input('{0}Dia = '.format(cores['verde'])))
mes = str(input('Mes = ')).title()
ano = int(input('Ano = '))
print('{3}Você nasceu no dia {4}{0}{3} de {4}{1}{3} de {4}{2}'.format(dia, mes, ano, cores['amarelo'], cores['azul'], cores['limpa']))
print('{}[ 1 ] Sim [ 2 ] Não'.format(cores['branco']))
resposta = int(input('{}Correto? '.format(cores['magenta'])))
sleep(1.5)
if resposta == 1:
    print('{}Então o programa funcionou corretamente!'.format(cores['verde']))
elif resposta == 2:
    print('{}Como assim vei? tu so pode ter digitado errado!'.format(cores['vermelho']))
else:
    print('{}Mano tu tem que digitar [ 1 ] ou [ 2 ]!'.format(cores['vermelho1']))
