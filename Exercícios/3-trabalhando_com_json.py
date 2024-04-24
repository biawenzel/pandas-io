'''Este DataFrame possui 6 colunas: genus (gênero), name (nome), id, family (família), order (ordem) e nutritions (nutrições). Note que a coluna nutritions está com todas as informações nutricionais aninhadas. Portanto, os dados precisam ser normalizados.
O desafio agora é normalizar esse DataFrame.'''

import requests, json, pandas as pd

url = 'https://fruityvice.com/api/fruit/all'

dados_frutas = requests.get(url)
resultado = json.loads(dados_frutas.text)
frutas = pd.DataFrame(resultado) #coluna 'nutritions' está aninhada

frutas_normalizado = pd.json_normalize(resultado)
print(frutas_normalizado)