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
    """
    Define como um produto será retornado
    """

    id: int = 1
    nome: str = "Nirvana Mini - Lavanda"
    quantidade: int = 10
    tipo: str = "Incenso"
    data_incersao: datetime = "Sat, 06 Sep 2025 14:55:59 GMT"
    data_atualizacao: datetime = "Sat, 06 Sep 2025 14:55:59 GMT"
    
def apresenta_produto(produto: Produto):
    """
    Retorna uma representação do produto seguindo o schema definido em ProdutoViewSchema.
    """

    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "tipo": produto.tipo,
        "data_incersao": produto.data_incersao,
        "data_atualizacao": produto.data_atualizacao
    }

class ProdutoBuscaSchema(BaseModel):
    """
    Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no nome do produto.
    """
    nome: str = "Nirvana Mini - Lavanda"

class ListaProdutosSchema(BaseModel):
    """
    Define como uma lista de produtos é retornada.
    """
    produtos:List[ProdutoViewSchema]   

def apresenta_produtos(produtos: List[Produto]):
    """
    Retorna uma lista de produtos seguindo o schema definido em ListaProdutosViewSchema e ProdutoViewSchema.
    """
    lista = []

    for produto in produtos:
        lista.append({
            "id": produto.id,
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "tipo": produto.tipo,
            "data_incersao": produto.data_incersao,
            "data_atualizacao": produto.data_atualizacao
            })
        
    return {"produtos": lista}

class ProdutoDelSchema(BaseModel):
    """
    Define como é a estrutura retornada após uma requisição de remoção
    """
    mensagem: str
    nome: str

class ProdutoUpdateSchema(BaseModel):
    """
    Define como um produto a ser atualizado deve ser representado
    
    Deixe nome_novo vazio caso não deseje alterá-lo.
    Deixe quantidade_nova com valor "-1" caso não deseje alterá-lo.
    Deixe quantidade_nova vazio caso não deseje alterá-lo.

    """
    nome: str = "Nirvana Mini - Lavanda"
    nome_novo: str = ""
    quantidade_nova: int = -1
    tipo_novo: str = ""

class ProdutoUpdateViewSchema(BaseModel):
    """
    Define a estrutura retornada após uma requisição de Update
    """
    mensagem: str