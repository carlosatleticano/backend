from config import *
from models.conexao import ConnModel
import uuid


class ClienteModel():
    def __init__(self, cpf,nome,email,dataDeNascimento,genero,rendaMensal):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.dataDeNascimento = dataDeNascimento
        self.genero = genero
        self.rendaMensal = rendaMensal




    def save_cliente(self):
        conn = ConnModel.conectar()
        cursor = conn.cursor()

        sql = "Select cpf from cad_cliente Where cpf = '{}'".format(self.cpf)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if resultado:
            return(409)

        id = str(uuid.uuid4())
        print(id)
        sql = "insert into cad_cliente (id, cpf,nome,email,dataDeNascimento,genero,rendaMensal) values ('{}', '{}','{}','{}','{}'::timestamp,'{}','{}'::numeric)".format(id, self.cpf,self.nome,self.email,self.dataDeNascimento,self.genero,self.rendaMensal)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return(id)
