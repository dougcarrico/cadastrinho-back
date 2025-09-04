from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

class ProdutoSchema(BaseModel):
    """
    Define como um novo produto a ser inserido deve ser representado
    """

    nome: str = "Nirvana Mini - Lavanda"
    quantidade: int = 10
    tipo: str = "Incenso"

class ProdutoViewSchema(BaseModel):
    """Define como um produto será retornado"""

    id: int = 1
    nome: str = "Nirvana Mini - Lavanda"
    quantidade: int = 10
    tipo: str = "Incenso"
    data_insercao: datetime = "DateTimeExemplo"
    data_atualizacao: datetime = "DateTimeExemplo"

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em ProdutoViewSchema.

    """

    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "tipo": produto.tipo,
        "data_insercao": produto.data_insercao,
        "data_atualizacao": produto.data_atualizacao
    }