from config import *
from models.conexao import ConnModel
import uuid
from datetime import datetime

class AporteModel():
    def __init__(self, idCliente, idPlano, aporte):
       self.idCliente=idCliente
       self.idPlano=idPlano
       self.aporte=aporte

    def find_contratacao(self):
        conn = ConnModel.conectar()
        cursor = conn.cursor()
        sql = "Select c.id, valorminimoaporteextra from cad_contratacao c join cad_produto p on p.id = c.idproduto Where idcliente = '{}' and c.id = '{}' ".format(self.idCliente, self.idPlano)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        if not resultado:
            return('Contratação não existe!')
        for linha in resultado:
            print (linha[1] , self.aporte)
            if self.aporte < linha[1]:
                return("Aporte insuficiente!")
        return(None)

    def save_aporte(self):
        conn = ConnModel.conectar()
        cursor = conn.cursor()
        id = str(uuid.uuid4())
        sql = "insert into cad_aporte (id, idplano, aporte) values ('{}','{}',{})".format(id, self.idPlano, self.aporte)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return([200,id])

