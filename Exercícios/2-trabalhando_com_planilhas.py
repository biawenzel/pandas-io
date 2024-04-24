'''Neste desafio, a sua função é efetuar a leitura desse link do Google Planilhas e depois salvar o DataFrame obtido no formato CSV. Pronto(a) para começar?'''

import pandas as pd

#https://docs.google.com/spreadsheets/d/1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw/edit#gid=1214654498
sheet_id = '1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'

emissoes_carbono_mundo = pd.read_csv(url)
emissoes_carbono_mundo.to_csv('dados_emissoes_carbono_mundo', index=False)