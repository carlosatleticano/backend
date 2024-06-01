from config import *
from models.conexao import ConnModel
from datetime import datetime

def find_cliente_by_id(id):
        conn = ConnModel.conectar()
        cursor = conn.cursor()
        # verifica se o cliente existe
        sql = "Select nome from cad_cliente Where id = '{}'".format(id)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        if not resultado:
            return('Cliente não existe!')
        return(None)

def find_produto_by_regras(aporte,idProduto,idCliente):
        conn = ConnModel.conectar()
        cursor = conn.cursor()
        # verifica se o produto existe
        sql = "select p.nome , case when expiracaodevenda >= now() then 'Produto com prazo de venda expirado.' when (valorMinimoAporteInicial > {}::numeric)  then 'Valor do aporte menor que o valor mínimo exigido' when (idadeDeEntrada > extract(year from age(datadenascimento))::int) then 'Idade inferior a idade mínima exigida' when (idadeDesaida < extract(year from age(datadenascimento))::int) then 'Idade superior a idade máxima exigida' end as erro from cad_produto p , cad_cliente c where p.id = '{}' and c.id = '{}'".format(aporte,idProduto,idCliente)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        if not resultado:
            return('Produto não existe!')
        else:
            for linha in resultado:
               return(linha[1])
        return(None)


