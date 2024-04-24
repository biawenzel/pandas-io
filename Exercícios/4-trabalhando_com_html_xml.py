'''Ao pesquisar na internet, Vanessa encontrou uma tabela de estimativas populacionais em um artigo da página Wikipédia. Assim como Vanessa, seu desafio é obter um DataFrame da tabela que contém as informações do número de habitantes de cada país.'''

import pandas as pd

url = 'https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o'
dados_pagina = pd.read_html(url)[0]
dados_pagina.drop('Unnamed: 0', axis=1, inplace=True)
print(dados_pagina)