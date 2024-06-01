from config import *
from models.conexao import ConnModel
import uuid
from datetime import datetime

class ResgateModel():
    def __init__(self, idPlano, resgate):
       self.idPlano=idPlano
       self.resgate=resgate

    def find_contratacao(self):
        conn = ConnModel.conectar()
        cursor = conn.cursor()
        sql = """select t.id
                      , aporte_inicial + aportes_extras - sum(coalesce(r.resgate,0)) < {}
                      , carencia_inicial_pendente
                      , (now()::date - max(r.data)) < 60 as carencia_parcial_de_resgate
                   from (select distinct c.id
                              , c.aporte aporte_inicial
                              , sum(coalesce(a.aporte,0)) over (partition by c.id) aportes_extras
                              , now()::date - c.datadacontratacao < p.carenciainicialderesgate as carencia_inicial_pendente
                           from cad_contratacao c 
                      left join cad_aporte a on c.id = a.idplano
                           join cad_produto p on p.id = c.idproduto 
                          where c.id = '{}'
                        ) t
                   left join cad_resgate r on r.idplano = t.id
                  group by t.id
                      , t.aporte_inicial
                      , t.aportes_extras
                      , carencia_inicial_pendente
              """.format(self.resgate, self.idPlano)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        if not resultado:
            return('Contratação não existe!')
        for linha in resultado:
            if linha[1]:
                return("Saldo insuficiente!")
            if linha[2]:
                return("Carncia inicial do plano não atendida!")
            if linha[3]:
                return("Carência após o último resgate não atendida!")
        return(None)


    def save_resgate(self):
        conn = ConnModel.conectar()
        cursor = conn.cursor()
        id = str(uuid.uuid4())
        sql = "insert into cad_resgate (id, idplano, resgate) values ('{}','{}',{})".format(id, self.idPlano, self.resgate)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return([200,id])

