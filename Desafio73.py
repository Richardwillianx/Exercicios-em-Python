"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Flamengo."""

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico - PR',
         'São Paulo', 'Internacional', 'Corithians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético - MG', 'Fluminense', 'Botafogo',
         'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print('*='*35)
print(f'Lista de times{times}')
print('*='*35)
print(f'Os cincos primeiros times são: {(times[0:5])}')
print('*='*35)
print(f'Os ultimos quatros colocados são: {(times[-4:])} ')
print('*='*35)
print(f'Em ordem alfabética: {sorted(times)}')
print('*='*35)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição!')