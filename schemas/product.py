from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from model.product import Product

class ProductSchema(BaseModel):
    """
    Define como um novo produto a ser inserido deve ser representado
    """

    name: str = "Nirvana Mini - Lavanda"
    quantity: int = 10
    type: str = "Incenso"

class ProductViewSchema(BaseModel):
    """
    Define como um produto será retornado
    """

    id: int = 1
    name: str = "Nirvana Mini - Lavanda"
    quantity: int = 10
    type: str = "Incenso"
    date_created: datetime = "Sat, 06 Sep 2025 14:55:59 GMT"
    date_updated: datetime = "Sat, 06 Sep 2025 14:55:59 GMT"
    
def show_product(product: Product):
    """
    Retorna uma representação do produto seguindo o schema definido em ProductViewSchema.
    """

    return {
        "id": product.id,
        "name": product.name,
        "quantity": product.quantity,
        "type": product.type,
        "date_created": product.date_created,
        "date_updated": product.date_updated
    }

class ProductSearchSchema(BaseModel):
    """
    Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no name do produto.
    """
    name: str = "Nirvana Mini - Lavanda"

class ProductListSchema(BaseModel):
    """
    Define como uma lista de produtos é retornada.
    """
    products:List[ProductViewSchema]   

def show_products(products: List[Product]):
    """
    Retorna uma lista de produtos seguindo o schema definido em ListaProdutosViewSchema e ProductViewSchema.
    """
    product_list = []

    for product in products:
        product_list.append({
            "id": product.id,
            "name": product.name,
            "quantity": product.quantity,
            "type": product.type,
            "date_created": product.date_created,
            "date_updated": product.date_updated
            })
        
    return {"products": product_list}

class ProductDeleteSchema(BaseModel):
    """
    Define como é a estrutura retornada após uma requisição de remoção
    """
    message: str
    name: str

class ProductUpdateSchema(BaseModel):
    """
    Define como um produto a ser atualizado deve ser representado
    
    Deixe new_name vazio caso não deseje alterá-lo.
    Deixe new_quantity com valor "-1" caso não deseje alterá-lo.
    Deixe new_quantity vazio caso não deseje alterá-lo.

    """
    name: str = "Nirvana Mini - Lavanda"
    new_name: str = ""
    new_quantity: int = -1
    new_type: str = ""

class ProductUpdateViewSchema(BaseModel):
    """
    Define a estrutura retornada após uma requisição de Update
    """
    message: str