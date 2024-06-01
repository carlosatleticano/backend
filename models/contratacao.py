from config import *
from models.conexao import ConnModel
import uuid
from datetime import datetime
from functions.functions import find_cliente_by_id
from functions.functions import find_produto_by_regras



class ContratacaoModel():
    def __init__(self, idCliente, idProduto, aporte, dataDaContratacao, idadeDeAposentadoria):
       self.idCliente=idCliente
       self.idProduto=idProduto
       self.aporte=aporte
       self.dataDaContratacao=dataDaContratacao
       self.idadeDeAposentadoria=idadeDeAposentadoria

   

    def save_contratacao(self):
        erro = find_cliente_by_id(self.idCliente)
        if erro != None:
            return([409,erro])
        erro = find_produto_by_regras(self.aporte,self.idProduto,self.idCliente)
        if erro != None:
            return([409,erro])
        conn = ConnModel.conectar()
        cursor = conn.cursor()
        id = str(uuid.uuid4())
        sql = "insert into cad_contratacao (id, idCliente, idProduto, aporte, dataDaContratacao, idadeDeAposentadoria) values ('{}','{}','{}',{},'{}',{})".format(id, self.idCliente, self.idProduto, self.aporte, self.dataDaContratacao, self.idadeDeAposentadoria)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return([200,id])

