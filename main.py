# pip install flask
# API

from flask import Flask, jsonify, request
from db import *

app = Flask(__name__)

# 1° rota

@app.route('/barbeiros', methods=['GET'])     # GET para buscar informação no banco

def buscarBarbeiros():
  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM barbeiros")   # executando a query
  lista_de_barbeiros = cursor.fetchall()      # guardando alista com a consulta

  lista_pro_json = []
  for barbeiro_da_vez in lista_de_barbeiros:
    novo_dicionario = {
      'id': barbeiro_da_vez[0],
      'nome': barbeiro_da_vez[1],
      'cpf': barbeiro_da_vez[2],
      'telefone': barbeiro_da_vez[3]
    }
    lista_pro_json.append(novo_dicionario)

  cursor.close()
  conexao.close()
  return jsonify(lista_pro_json)              # transformando em json() a lista

# 2° rota

@app.route('/servicos', methods=['GET'])      # GET para buscar informação no banco

def buscarServicos():
  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM servicos")   # executando a query
  lista_de_servicos = cursor.fetchall()      # guardando alista com a consulta

  lista_pro_json = []
  for servicos_da_vez in lista_de_servicos:
    novo_dicionario = {
      'id': servicos_da_vez[0],
      'nome': servicos_da_vez[1],
      'descricao': servicos_da_vez[2],
      'valor': servicos_da_vez[3],
      'porcentagem_barbeiro': servicos_da_vez[4],
    }
    lista_pro_json.append(novo_dicionario)

  cursor.close()
  conexao.close()
  return jsonify(lista_pro_json)          # transformando em json() a lista

# 3° rota

@app.route('/atendimentos', methods=['GET'])     # GET para buscar informação no banco

def buscarAtendimentos():
  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM atendimentos")   # executando a query
  lista_de_atendimentos = cursor.fetchall()      # guardando alista com a consulta

  lista_pro_json = []
  for atendimentos_da_vez in lista_de_atendimentos:
    novo_dicionario = {
      'id': atendimentos_da_vez[0],
      'data_atendimento': atendimentos_da_vez[1],
      'id_barbeiro': atendimentos_da_vez[2],
      'id_servico': atendimentos_da_vez[3]     
    }
    lista_pro_json.append(novo_dicionario)
  
  cursor.close()
  conexao.close()
  return jsonify(lista_pro_json)          # transformando em json() a lista



if __name__ == "__main__":
  app.run(debug=True) 