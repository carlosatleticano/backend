from flask_restful import Resource, reqparse
from models.cliente import ClienteModel

atributos = reqparse.RequestParser()
atributos.add_argument('cpf', type=str, required=True)
atributos.add_argument('nome', type=str, required=True)
atributos.add_argument('email', type=str, required=True)
atributos.add_argument('dataDeNascimento', type=str,  required=True)
atributos.add_argument('genero', type=str,  required=True)
atributos.add_argument('rendaMensal', type=str, required=True)

class CadastroCliente(Resource):
    def post(self):
        dados = atributos.parse_args()
        cliente = ClienteModel(**dados)
        retorno = cliente.save_cliente()
        if retorno == 409:
           return {"message": "O cliente ja esta cadastrado!"} , 409 #conflict
        return{"id":retorno}, 200



