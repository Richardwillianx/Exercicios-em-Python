#print('\033[7;33;44m Olá, Mundo!\033[m')

"""a = 3
b = 5
print('Os valores são \033[34;40m{}\033[m e \033[31;40m{}\033[m!!'.format(a, b))"""

nome = 'Richard'

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

#print('Olá! muito prazer em lhe conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

print('Olá! muito prazer em lhe conhecer, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))
