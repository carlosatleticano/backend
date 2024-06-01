from flask_restful import Resource, reqparse
from models.contratacao import ContratacaoModel

atributos = reqparse.RequestParser()
atributos.add_argument('idCliente', type=str, required=True)
atributos.add_argument('idProduto', type=str, required=True)
atributos.add_argument('aporte', type=float,  required=True)
atributos.add_argument('dataDaContratacao', type=str, required=True)
atributos.add_argument('idadeDeAposentadoria', type=int, required=True)


class CadastroContratacao(Resource):
    def post(self):
        dados = atributos.parse_args()
        contratacao = ContratacaoModel(**dados)
        retorno = contratacao.save_contratacao()
        if retorno[0]  == 200:
            return {"id": retorno[1]} , 200
        return {"erro": retorno[1]} , retorno[0]



