from flask_restful import Resource, reqparse
from models.produto import ProdutoModel

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True)
atributos.add_argument('susep', type=str, required=True)
atributos.add_argument('expiracaoDeVenda', type=str,  required=True)
atributos.add_argument('valorMinimoAporteInicial', type=float,  required=True)
atributos.add_argument('valorMinimoAporteExtra', type=float, required=True)
atributos.add_argument('idadeDeEntrada', type=int, required=True)
atributos.add_argument('idadeDeSaida', type=int, required=True)
atributos.add_argument('carenciaInicialDeResgate', type=int, required=True)
atributos.add_argument('carenciaEntreResgates', type=int, required=True)

class CadastroProduto(Resource):
    def post(self):
        dados = atributos.parse_args()
        produto = ProdutoModel(**dados)
        retorno = produto.save_produto()
        if retorno == 409:
           return {"message": "O produto ja esta cadastrado"} , 409 #conflict
        return{"id":retorno}, 200

