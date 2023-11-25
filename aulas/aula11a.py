nome = 'Rodrigo'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'preto_e_branco': '\033[7;1;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['preto_e_branco'], nome, cores['limpa']))