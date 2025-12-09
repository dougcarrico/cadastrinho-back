from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from model.product import Product

class ProductSchema(BaseModel):
    """
    Define como um novo produto a ser inserido deve ser representado
    """

    nome: str = "Nirvana Mini - Lavanda"
    quantidade: int = 10
    tipo: str = "Incenso"

class ProductViewSchema(BaseModel):
    """
    Define como um produto será retornado
    """

    id: int = 1
    nome: str = "Nirvana Mini - Lavanda"
    quantidade: int = 10
    tipo: str = "Incenso"
    data_incersao: datetime = "Sat, 06 Sep 2025 14:55:59 GMT"
    data_atualizacao: datetime = "Sat, 06 Sep 2025 14:55:59 GMT"
    
def show_product(product: Product):
    """
    Retorna uma representação do produto seguindo o schema definido em ProductViewSchema.
    """

    return {
        "id": product.id,
        "nome": product.nome,
        "quantidade": product.quantidade,
        "tipo": product.tipo,
        "data_incersao": product.data_incersao,
        "data_atualizacao": product.data_atualizacao
    }

class ProductSearchSchema(BaseModel):
    """
    Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no nome do produto.
    """
    nome: str = "Nirvana Mini - Lavanda"

class ProductListSchema(BaseModel):
    """
    Define como uma lista de produtos é retornada.
    """
    products:List[ProductViewSchema]   

def show_products(products: List[Product]):
    """
    Retorna uma lista de produtos seguindo o schema definido em ListaProdutosViewSchema e ProductViewSchema.
    """
    lista = []

    for product in products:
        lista.append({
            "id": product.id,
            "nome": product.nome,
            "quantidade": product.quantidade,
            "tipo": product.tipo,
            "data_incersao": product.data_incersao,
            "data_atualizacao": product.data_atualizacao
            })
        
    return {"products": lista}

class ProductDeleteSchema(BaseModel):
    """
    Define como é a estrutura retornada após uma requisição de remoção
    """
    mensagem: str
    nome: str

class ProductUpdateSchema(BaseModel):
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

class ProductUpdateViewSchema(BaseModel):
    """
    Define a estrutura retornada após uma requisição de Update
    """
    mensagem: str