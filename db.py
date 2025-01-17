# conectando com o db

# pip install mysql-connector-python
# pip install psycopg2  // para instal com o postgreSQL

import psycopg2;   # para conectar ao pgAdmin

host = 'localhost'
data = 'barbeariaReactPython'
user = 'postgres'
password = '123456'
port = '5432'

def fazerConexao():
  try:
    conn = psycopg2.connect(
      host = host,
      database = data,
      user = user,
      password = password,
      port = port,
    )
    return conn

  except:
    return 'Falha ao conectar ao banco'