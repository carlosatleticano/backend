import pytest
from app import get_age
from models.contratacao import find_cliente_by_id
from models.contratacao import find_produto_by_regras

def test_get_age():
    # Given.
    yyyy, mm, dd = map(int, "1970/08/08".split("/"))   
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    assert age == 54


def test_find_cliente_by_id():
    cliente = "31965d43-322f-41b7-95e4-b8c36acdd0b0"
    erro = find_cliente_by_id(cliente)
    assert erro == None    

def test_find_produto_by_regras():
    produto = "ae029fc3-1d03-47f7-8e08-543aed438044"
    aporte = 2000.00
    cliente = "31965d43-322f-41b7-95e4-b8c36acdd0b0"
    erro = find_produto_by_regras(aporte,produto,cliente)
    assert erro == None    
    produto = "zzz"
    erro = find_produto_by_regras(aporte,produto,cliente)
    assert erro == "Produto não existe!"    
    aporte = 0.00
    produto = "ae029fc3-1d03-47f7-8e08-543aed438044"
    erro = find_produto_by_regras(aporte,produto,cliente)
    assert erro == "Valor do aporte menor que o valor mínimo exigido"


