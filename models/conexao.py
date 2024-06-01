import psycopg2
from config import *

class ConnModel():
    def __init__(self, conexao) :
        self.conexao = conexao

    @classmethod
    def conectar(cls):
        conexao = psycopg2.connect(user=user_conn, password=senha_conn, host= host_conn, port=porta_conn, database=banco_conn, sslmode = 'disable')
        return conexao

    def desconectar(self):
        self.close()
