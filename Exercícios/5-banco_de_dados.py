'''Você é responsável por criar um banco de dados local de clientes para uma instituição financeira. Temos o arquivo CSV com os dados de clientes. Sua missão é:
1. Criar o banco de dados local com a biblioteca SQLAlchemy.
2. Escrever os dados do arquivo CSV neste banco de dados local.
3. Realizar três atualizações no banco de dados:
    - Atualizar o registro do cliente de ID 6840104 que teve o rendimento anual alterado para 300000.
    - Excluir o registro do cliente de ID 5008809, pois essa pessoa não possui mais conta na instituição financeira.
    - Criar um novo registro de cliente seguindo as especificações abaixo:
        ID_Cliente: 6850985
        Idade: 33
        Grau_escolaridade: Doutorado
        Estado_civil: Solteiro
        Tamanho_familia: 1
        Categoria_de_renda: Empregado
        Ocupacao: TI
        Anos_empregado: 2
        Rendimento_anual: 290000
        Tem_carro: 0
        Moradia: Casa/apartamento próprio'''

import sqlalchemy, pandas as pd
from sqlalchemy import create_engine, MetaData, Table, inspect, text

#sqlalchemy.__version__

#Criando o banco de dados local
engine = create_engine('sqlite:///:memory:', future=True)

#Carregando os dados
url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'
dados = pd.read_csv(url)

#Escrevendo os dados do CSV no banco de dados
dados.to_sql('clientes_banco', engine, index=False)

#Atualizando o registro do cliente de ID 6840104 que teve o rendimento anual alterado para 300000
query = 'UPDATE clientes_banco SET Rendimento_anual=300000.0 WHERE ID_Cliente=6840104'
with engine.connect() as conn:
  conn.execute(text(query))
  conn.commit()

#Excluir o registro do cliente de ID 5008809
query = 'DELETE FROM clientes_banco WHERE ID_Cliente=5008809'
with engine.connect() as conn:
  conn.execute(text(query))
  conn.commit()

#Criar um novo registro de cliente seguindo as especificações
query = 'INSERT INTO clientes_banco (ID_Cliente, Idade, Grau_escolaridade, Estado_civil, ' \
        'Tamanho_familia, Categoria_de_renda, Ocupacao, Anos_empregado, ' \
        'Rendimento_anual, Tem_carro, Moradia) ' \
        'VALUES (6850985, 33, "Doutorado", "Solteiro", 1, "Empregado", "TI", ' \
        '2, 290000, 0, "Casa/apartamento próprio")'
with engine.connect() as conn:
  conn.execute(text(query))
  conn.commit()

print(pd.read_sql_table('clientes_banco', engine))
