from config import *
from models.conexao import ConnModel
import uuid


class ProdutoModel():
    def __init__(self,nome,susep,expiracaoDeVenda,valorMinimoAporteInicial,valorMinimoAporteExtra,idadeDeEntrada,idadeDeSaida,carenciaInicialDeResgate,carenciaEntreResgates):
       self.nome=nome
       self.susep=susep
       self.expiracaoDeVenda=expiracaoDeVenda
       self.valorMinimoAporteInicial=valorMinimoAporteInicial
       self.valorMinimoAporteExtra=valorMinimoAporteExtra
       self.idadeDeEntrada=idadeDeEntrada
       self.idadeDeSaida=idadeDeSaida
       self.carenciaInicialDeResgate=carenciaInicialDeResgate
       self.carenciaEntreResgates=carenciaEntreResgates



    def save_produto(self):
        conn = ConnModel.conectar()
        cursor = conn.cursor()

        sql = "Select nome from cad_produto Where nome = '{}'".format(self.nome)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if resultado:
            return(409)
        id = str(uuid.uuid4())
        sql = "insert into cad_produto (id, nome,susep,expiracaoDeVenda,valorMinimoAporteInicial,valorMinimoAporteExtra,idadeDeEntrada,idadeDeSaida,carenciaInicialDeResgate,carenciaEntreResgates) values ('{}', '{}','{}','{}'::date,'{}'::numeric,'{}'::numeric,'{}'::int,'{}'::int,'{}'::int,'{}'::int)".format(id, self.nome,self.susep,self.expiracaoDeVenda,self.valorMinimoAporteInicial,self.valorMinimoAporteExtra,self.idadeDeEntrada,self.idadeDeSaida,self.carenciaInicialDeResgate,self.carenciaEntreResgates)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return(id)
