from flask import Flask, jsonify
from flask_restful import Api
from resources.cliente import CadastroCliente
from resources.produto import CadastroProduto
from resources.contratacao import CadastroContratacao
from resources.aporte import CadastroAporte
from resources.resgate import CadastroResgate
from config import *
import datetime

app = Flask(__name__)


api = Api(app)


@app.route('/api')
def index():
    return '<h1>Bem vindo</h1>'

def get_age(yyyy:int, mm:int, dd:int) -> int:
    dob = datetime.date(yyyy, mm, dd)
    today = datetime.date.today()
    age = round((today - dob).days / 365.25)
    return age

#api.add_resource(User, '/api/usuarios/<int:user_id>')
api.add_resource(CadastroCliente, '/api/cliente')
api.add_resource(CadastroProduto, '/api/produto')
api.add_resource(CadastroContratacao, '/api/contratacao')
api.add_resource(CadastroAporte, '/api/aporte')
api.add_resource(CadastroResgate , "/api/resgate")
