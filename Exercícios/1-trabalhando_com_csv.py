'''1. Verifique se o arquivo CSV está separado por vírgula ou ponto e vírgula.
2. A codificação do arquivo é ISO-8859-1.
3. As três primeiras linhas linhas do arquivo podem ser desconsideradas, pois o cabeçalho só começa na quarta linha.
4. As 9 últimas linhas também podem ser desconsideradas, pois são apenas informações sobre onde os dados foram obtidos.
5. Para deletar as últimas linhas é necessário adicionar o parâmetro engine='python'.'''

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/dados_sus.csv'

dados_sus_df = pd.read_csv(url, sep=';', encoding='ISO-8859-1', skiprows=3, skipfooter=9, engine='python')
print(dados_sus_df)