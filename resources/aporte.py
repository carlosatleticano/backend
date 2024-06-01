from flask_restful import Resource, reqparse
from models.aporte import AporteModel

atributos = reqparse.RequestParser()
atributos.add_argument('idCliente', type=str, required=True)
atributos.add_argument('idPlano', type=str, required=True)
atributos.add_argument('aporte', type=float,  required=True)


class CadastroAporte(Resource):
    def post(self):
        dados = atributos.parse_args()
        aporte = AporteModel(**dados)
        erro = aporte.find_contratacao()
        if erro != None:
            return([409,erro])
        retorno = aporte.save_aporte()
        if retorno[0]  == 200:
            return {"id": retorno[1]} , 200
        return {"erro": retorno[1]} , retorno[0]



