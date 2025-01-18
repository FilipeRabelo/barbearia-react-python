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
  lista_de_barbeiros = cursor.fetchall()      # guardando a lista com a consulta

  # para transformar em dicionario / objeto json()
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


@app.route('/barbeiros', methods=['POST'])    # POST para enviar - cadastrar

def adicionarBarbeiro():
  data = request.get_json()                   # pegando as infos enviadas e guardando na variavel data
  nome = data['nome']
  cpf = data['cpf']
  telefone = data['telefone']

  conexao = fazerConexao()
  cursor = conexao.cursor()

  query = "INSERT INTO barbeiros (nome, cpf, telefone) VALUES (%s, %s, %s)"
  cursor.execute(query, (nome, cpf, telefone))
  conexao.commit()                            
  cursor.close()
  conexao.close()
  return jsonify({"Mensagem": "Barbeiro cadastrado com sucesso!"})

  # cursor.execute(f"INSERT INTO barbeiros (nome, cpf, telefone) VALUES ('{nome}', '{cpf}', '{telefone}')")
  # commit para salvar


@app.route('/barbeiros/<int:id>', methods=['PUT'])    # POST para atualizar 

def atualizarBarbeiro(id):
  data = request.get_json()                  # pegando as infos enviadas e guardando na variavel data
  nome = data['nome']
  cpf = data['cpf']
  telefone = data['telefone']

  conexao = fazerConexao()
  cursor = conexao.cursor()

  query = "UPDATE barbeiros SET nome = %s, cpf = %s, telefone = %s WHERE id = %s"
  cursor.execute(query, (nome, cpf, telefone, id))
  conexao.commit()                            
  cursor.close()
  conexao.close()
  return jsonify({"Mensagem": "Barbeiro Atualizado com sucesso!"})


@app.route('/barbeiros/<int:id>', methods=['DELETE'])    # POST para deletar 

def deletarBarbeiro(id):

  conexao = fazerConexao()
  cursor = conexao.cursor()

  query = "DELETE FROM barbeiro WHERE id = %s"
  cursor.execute(query, (id))
  conexao.commit()                            
  cursor.close()
  conexao.close()
  return jsonify({"Mensagem": "Barbeiro Deletado com sucesso!"})

# --------------------------------------------------------------------------


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


@app.route('/servicos', methods=['POST'])    # POST para enviar - cadastrar

def adicionarServicos():
  data = request.get_json()                   # pegando as infos enviadas e guardando na variavel data
  nome = data['nome']
  descricao = data['descricao']
  valor = data['valor']
  porcentagem_barbeiro = data['porcentagem_barbeiro']

  conexao = fazerConexao()
  cursor = conexao.cursor()
  
  query = "INSERT INTO servicos (nome, descricao, valor, porcentagem_barbeiro) VALUES (%s, %s, %s, %s)"
  cursor.execute(query, (nome, descricao, valor, porcentagem_barbeiro))
  conexao.commit()                            
  cursor.close()
  conexao.close()
  return jsonify({"Mensagem": "Serviço cadastrado com sucesso!"})


@app.route('/servicos/<int:id>', methods=['PUT'])    # POST para atualizar 

def atualizarServicos(id):
  data = request.get_json()                  # pegando as infos enviadas e guardando na variavel data
  nome = data['nome']
  descricao = data['descricao']
  valor = data['valor']
  porcentagem_barbeiro = data['porcentagem_barbeiro']

  conexao = fazerConexao()
  cursor = conexao.cursor()

  query = "UPDATE servicos SET nome = %s, descricao = %s, valor = %s, porcentagem_barbeiro = %s WHERE id = %s"
  cursor.execute(query, (nome, descricao, valor, porcentagem_barbeiro))
  conexao.commit()                            
  cursor.close()
  conexao.close()
  return jsonify({"Mensagem": "Serviço Atualizado com sucesso!"})


@app.route('/servicos/<int:id>', methods=['DELETE'])    # POST para deletar 

def deletarServico(id):

  conexao = fazerConexao()
  cursor = conexao.cursor()

  query = "DELETE FROM servicos WHERE id = %s"
  cursor.execute(query, (id))
  conexao.commit()                            
  cursor.close()
  conexao.close()
  return jsonify({"Mensagem": "Serviço Deletado com sucesso!"})


# --------------------------------------------------------------------------


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


@app.route('/atendimentos', methods=['POST'])    # POST para enviar - cadastrar

def adicionarAtendimentos():
  data = request.get_json()                   # pegando as infos enviadas e guardando na variavel data
  data_atendimento = data['data_atendimento']
  id_barbeiro = data['id_barbeiro']
  id_servico = data['id_servico']

  conexao = fazerConexao()
  cursor = conexao.cursor()
  
  query = "INSERT INTO atendimentos (data_atendimento, id_barbeiro, id_servico) VALUES ( %s, %s, %s)"
  cursor.execute(query, (data_atendimento, id_barbeiro, id_servico))
  conexao.commit()                            
  cursor.close()
  conexao.close()
  return jsonify({"Mensagem": "Atendimento cadastrado com sucesso!"})


@app.route('/atendimentos/<int:id>', methods=['PUT'])    # POST para atualizar 

def atualizarAtendimentos(id):
  data = request.get_json()                  # pegando as infos enviadas e guardando na variavel data
  data_atendimento = data['data_atendimento']
  id_barbeiro = data['id_barbeiro']
  id_servico = data['id_servico']

  conexao = fazerConexao()
  cursor = conexao.cursor()

  query = "UPDATE atendimentos SET data_atendimento = %s, id_barbeiro = %s, id_servico = %s WHERE id = %s"
  cursor.execute(query, (data_atendimento, id_barbeiro, id_servico))
  conexao.commit()                            
  cursor.close()
  conexao.close()
  return jsonify({"Mensagem": "Atendimento Atualizado com sucesso!"})


@app.route('/atendimentos/<int:id>', methods=['DELETE'])    # POST para deletar 

def deletarAtendimentos(id):

  conexao = fazerConexao()
  cursor = conexao.cursor()

  query = "DELETE FROM atendimentos WHERE id = %s"
  cursor.execute(query, (id))
  conexao.commit()                            
  cursor.close()
  conexao.close()
  return jsonify({"Mensagem": "Atendimento Deletado com sucesso!"})





if __name__ == "__main__":
  app.run(debug=True) 