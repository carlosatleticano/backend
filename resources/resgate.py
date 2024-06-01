from flask_restful import Resource, reqparse
from models.resgate import ResgateModel

atributos = reqparse.RequestParser()
atributos.add_argument('idPlano', type=str, required=True)
atributos.add_argument('resgate', type=float,  required=True)


class CadastroResgate(Resource):
    def post(self):
        dados = atributos.parse_args()
        resgate = ResgateModel(**dados)
        erro = resgate.find_contratacao()
        if erro != None:
            return([409,erro])
        retorno = resgate.save_resgate()
        if retorno[0]  == 200:
            return {"id": retorno[1]} , 200
        return {"erro": retorno[1]} , retorno[0]



