from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy import update
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from model import Session
from model import Product
from schemas import * 
from flask_cors import CORS

from datetime import datetime

# Para poder fazer requisições para outras APIs
import requests

# Para definir variáveis de ambiente
import os
from dotenv import load_dotenv

# Carrega as variávels de ambiente do .env - Por padrão o load_dotenv() procura nas pastas filhas e pastas pai pelo .env
load_dotenv() 
shipping_calculate_token = os.getenv("SHIPPING_CALCULATE_TOKEN")

info = Info(title="API Cadastrinho", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
product_tag = Tag(name="Product", description="Adição de produto")
shipping_calculate_tag = Tag(name="Calculo de frete (Shipping Calculate)", description="Calculo de frete de um pacote")


@app.get('/', tags=[home_tag])
def home():
    """
    Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/product', tags=[product_tag],
          responses={"200": ProductViewSchema, "409": ErrorSchema, "400": ErrorSchema})

def add_product(form: ProductSchema):
    """
    Adiciona um novo produto à base de dados

    Retorna uma representação dos produtos
    """
    product = Product(name=form.name, 
                      quantity=form.quantity, 
                      type=form.type)
    
    try:
        # Cria uma conexão com o banco de dados
        session = Session()

        # Adiciona produto no banco de dados
        session.add(product)

        # Confirma comando de adição de novo item na tabela
        session.commit()

        return show_product(product), 200
    
    except IntegrityError as e:
        #Erro de integridade e qual a origem do erro
        error_message = f"Erro de integridade: {e.orig}"
        return {
            "message": error_message
        }, 409
    
    except Exception as e:
        #Erro genérico não previsto
        error_message = "O item não foi adicionado por um erro desconhecido"

        return {
            "message": error_message
        }, 400
    

@app.get('/product', tags=[product_tag],
          responses={"200": ProductViewSchema, "404": ErrorSchema})
def get_product(query: ProductSearchSchema):
    """
    Faz a busca por um produto
    """
    product_name = unquote(query.name)

    # Criando conexão com a base
    session = Session()

    # Fazendo a busca
    product = session.query(Product).filter(Product.name == product_name).first()

    # Se não encontrar o produto
    if not product:

        error_message = "Produto não encontrado"
        
        return {
            "message": error_message
            }, 404
    
    else:

       return show_product(product), 200
    

@app.get('/products', tags=[product_tag],
         responses={"200": ProductListSchema})

def get_products():
    """
    Faz a busca por todos os produtos cadastrados
    Retorna uma representação da listagem de todos.
    """

    # Criando conexão com a base
    session = Session()

    # Fazendo a busca
    products = session.query(Product).order_by("name").all()
       
    return show_products(products), 200


@app.delete('/product', tags=[product_tag],
            responses={"200": ProductDeleteSchema, "404": ErrorSchema})

def del_product(query: ProductSearchSchema):
    """
    Deleta um produto a partir do nome informado
    Retorna uma mensagem confirmando a remoção
    """
    product_name = unquote(query.name)

    session = Session()
    product_to_delete = session.query(Product).filter(Product.name == product_name).delete()
    session.commit()

    if product_to_delete:
        # Retorna mensagem de confirmação

        return {
            "message": "Produto Removido", 
            "name": product_name
        }, 200
    
    else:
        # Se o produto não foi encontrado
        error_message = "Produto não encontrado"

        return {
            "message": error_message
        }, 404
    

@app.put('/product', tags=[product_tag],
         responses={"200": ProductUpdateSchema, "400": ErrorSchema})

def product_update(form: ProductUpdateSchema):
    """
    Atualiza um produto a partir do name fornecido, atributo e valor do atributo a ser atualizado.
    """
    product_name = form.name

    if form.new_name:
        new_name = form.new_name
    else:
        new_name = Product.name

    if form.new_quantity >= 0:
        new_quantity = form.new_quantity
    else:
        new_quantity = Product.quantity

    if form.new_type:
        new_type = form.new_type
    else:
        new_type = Product.type

    try:
        session = Session()

        search_query = (select(Product.name).where(Product.name == product_name))
        search_result = session.execute(search_query).first()

        if not search_result:
            return {
                "message": "Produto não encontrado",
                }

        statement = (update(Product).where(Product.name == product_name).values(name=new_name, quantity=new_quantity, type=new_type, date_updated=datetime.now()))
        session.execute(statement)
        
        print("Produto atualizado")
        session.commit()
        return {
            "message": "Produto atualizado!"
        }, 200

    except IntegrityError as e:
        #Erro de integridade e qual a origem do erro
        error_message = f"Erro de integridade: {e.orig}"
        session.rollback()

        return {
            "message": error_message
        }, 409
    
    except Exception as e:
        #Erro genérico não previsto
        error_message = f"O item não foi atualizado. Erro: {e.__cause__}"
        session.rollback()

        return {
            "message": error_message
        }, 400
    

@app.post('/shipping_calculate', tags=[shipping_calculate_tag],
          responses={"200": ShippingCalculateViewSchema, "409": ErrorSchema, "400": ErrorSchema})

def shipping_calculate(form: ShippingCalculateSchema):
    """
    Envia requisição de calculo de frete para a API Melhor Envio.
    """
    from_postal_code = form.from_postal_code
    to_postal_code = form.to_postal_code
    package_height = form.package_height
    package_width = form.package_width
    package_length = form.package_length
    package_weight = form.package_weight

    try:
        url = "https://www.melhorenvio.com.br/api/v2/me/shipment/calculate"

        payload = {
            "from": { "postal_code": from_postal_code },
            "to": { "postal_code": to_postal_code },
            "package": {
                "height": package_height,
                "width": package_width,
                "length": package_length,
                "weight": package_weight
            }
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {shipping_calculate_token}",
            "User-Agent": "Aplicação (email para contato técnico)"
        }

        response = requests.post(url, json=payload, headers=headers)

        return response.json(), 200
    
    except Exception as e:
        #Erro genérico não previsto
        error_message = "Não foi possivel retornar as informacoes da API Melhor Envio"

        return {
            "message": error_message
        }, 400