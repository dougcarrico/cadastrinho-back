from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy import update
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from model import Session
from model import Produto
from schemas import * 
from flask_cors import CORS

from datetime import datetime

# Para poder fazer requisições para outras APIs
import requests

info = Info(title="API Cadastrinho", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

#definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
produto_tag = Tag(name="Produto", description="Adição de produto")
shipping_calculate_tag = Tag(name="Calculo de frete (Shipping Calculate)", description="Calculo de frete de um pacote")


@app.get('/', tags=[home_tag])
def home():
    """
    Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})

def add_produto(form: ProdutoSchema):
    """
    Adiciona um novo produto à base de dados

    Retorna uma representação dos produtos
    """
    produto = Produto(nome=form.nome, 
                      quantidade=form.quantidade, 
                      tipo=form.tipo)
    
    try:
        # Cria uma conexão com o banco de dados
        session = Session()

        # Adiciona produto no banco de dados
        session.add(produto)

        # Confirma comando de adição de novo item na tabela
        session.commit()

        return apresenta_produto(produto), 200
    
    except IntegrityError as e:
        #Erro de integridade e qual a origem do erro
        error_msg = f"Erro de integridade: {e.orig}"
        return {
            "mensagem": error_msg
        }, 409
    
    except Exception as e:
        #Erro genérico não previsto
        error_msg = "O item não foi adicionado por um erro desconhecido"

        return {
            "mensagem": error_msg
        }, 400
    

@app.get('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaSchema):
    """
    Faz a busca por um produto
    """
    produto_nome = unquote(query.nome)

    # Criando conexão com a base
    session = Session()

    # Fazendo a busca
    produto = session.query(Produto).filter(Produto.nome == produto_nome).first()

    # Se não encontrar o produto
    if not produto:

        error_msg = "Produto não encontrado"
        
        return {
            "mesage": error_msg
            }, 404
    
    else:

       return apresenta_produto(produto), 200
    

@app.get('/produtos', tags=[produto_tag],
         responses={"200": ListaProdutosSchema})

def get_produtos():
    """
    Faz a busca por todos os produtos cadastrados
    Retorna uma representação da listagem de todos.
    """

    # Criando conexão com a base
    session = Session()

    # Fazendo a busca
    produtos = session.query(Produto).order_by("nome").all()
       
    return apresenta_produtos(produtos), 200


@app.delete('/produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})

def del_produto(query: ProdutoBuscaSchema):
    """
    Deleta um produto a partir do nome informado
    Retorna uma mensagem confirmando a remoção
    """
    produto_nome = unquote(query.nome)

    session = Session()
    deleta = session.query(Produto).filter(Produto.nome == produto_nome).delete()
    session.commit()

    if deleta:
        # Retorna mensagem de confirmação

        return {
            "mensagem": "Produto Removido", 
            "nome": produto_nome
        }, 200
    
    else:
        # Se o produto não foi encontrado
        error_msg = "Produto não encontrado"

        return {
            "mensagem": error_msg
        }, 404
    

@app.put('/produto', tags=[produto_tag],
         responses={"200": ProdutoUpdateSchema, "400": ErrorSchema})

def produto_update(form: ProdutoUpdateSchema):
    """
    Atualiza um produto a partir do nome fornecido, atributo e valor do atributo a ser atualizado.
    """
    produto_nome = form.nome

    if form.nome_novo:
        nome_novo = form.nome_novo
    else:
        nome_novo = Produto.nome

    if form.quantidade_nova >= 0:
        quantidade_nova = form.quantidade_nova
    else:
        quantidade_nova = Produto.quantidade

    if form.tipo_novo:
        tipo_novo = form.tipo_novo
    else:
        tipo_novo = Produto.tipo

    try:
        session = Session()

        search_query = (select(Produto.nome).where(Produto.nome == produto_nome))
        search_result = session.execute(search_query).first()

        if not search_result:
            return {
                "mensagem": "Produto não encontrado",
                }

        statement = (update(Produto).where(Produto.nome == produto_nome).values(nome=nome_novo, quantidade=quantidade_nova, tipo=tipo_novo, data_atualizacao=datetime.now()))
        session.execute(statement)
        
        print("Produto atualizado")
        session.commit()
        return {
            "mensagem": "Produto atualizado!"
        }, 200

    except IntegrityError as e:
        #Erro de integridade e qual a origem do erro
        error_msg = f"Erro de integridade: {e.orig}"
        session.rollback()

        return {
            "mensagem": error_msg
        }, 409
    
    except Exception as e:
        #Erro genérico não previsto
        error_msg = f"O item não foi atualizado. Erro: {e.__cause__}"
        session.rollback()

        return {
            "mensagem": error_msg
        }, 400
    

@app.post('/shipping_calculate', tags=[shipping_calculate_tag],
          responses={"200": ShippingCalculateViewSchema, "409": ErrorSchema, "400": ErrorSchema})

def shipping_calculate(form: ShippingCalculateSchema):
    """
    Envia requisição de calculo de frete para a API Melhor Envio.
    """
    from_postal_code = str(form.from_postal_code)
    to_postal_code = str(form.to_postal_code)
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
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNjRjYmNlZjI5MTU1NmJmNWFjYzgzODFjNzIxNWY4NDIxODM0NjgxNDBlYTU1OWExNjYwNmE0ZTUzZmQzZmMxYWRmYzk5NGJjMGExMjlmY2IiLCJpYXQiOjE3NjQ1MTkyNTYuMTc5MjYxLCJuYmYiOjE3NjQ1MTkyNTYuMTc5MjYyLCJleHAiOjE3OTYwNTUyNTYuMTY2MjA3LCJzdWIiOiJhMDdiNWVhOS0wNGIzLTQzMzYtODFlNC0yNDk0YTczM2I4NjEiLCJzY29wZXMiOlsic2hpcHBpbmctY2FsY3VsYXRlIl19.KTaeSWtqfa5gfWLJQ7C0azRomWQXxC5KIt3R7z1BOpvtRVtjEFRsyRZH8tMsxs8dFKhbWl0B2bfV59gD_qJvz_lwN6st9mT-35k2B8axJQ6d5Kngu1g85B2yrXukbGNmmc3etaOJafvkdG1TIIoiM2qzbJVYRvWr8sdGEDXj4wHmlesIHMTlJb5mIW3rbC2bPqUKT-j1kIF_7xK7mKYM0v1UkTJVxr1TlSk5Kkw5dFyEUwfnM45NgFUn_ziVfnPyqivLivkjSOdUoAmSO3nHqZIj0mkK3lyDdj8QYOduRBg7MW0RpEafZbGnAGxfEVF-dbnMgQh9oJXP-otzZBdTurhVpD-KHjsl38q7ltNZmZGNGpUHqsw-7JYcRBHL7YuawMJfQ30NYTDQG0bliK0r04_2ccAYB9df8Zt9WkuQpfGEWr77suszGnweGH2kMqoWaWRyboHftViqRh6E6xdn9jaSinzvSH9f9SAkdAJv7VwOJE6zJqaB1iejBmuG7Z6FM56XSV7-HWQp_WcE472Ek0lV45FoLBNHl8N1TJYqIB8RM0LoRe2ZuBcZUQbCGpUnubM1g2A2woOJyCTQeRtq1v_CGS91Ljv2FWAmBAhyBfF_qv847EFexBcTeHSxktsJfpQJ0lU8BvmMeT8mYuLK_Rqc2r4gqYNBx9_NfBGla_E",
            "User-Agent": "Aplicação (email para contato técnico)"
        }

        response = requests.post(url, json=payload, headers=headers)

        return response.json(), 200
    
    except Exception as e:
        #Erro genérico não previsto
        error_msg = "Não foi possivel retornar as informacoes da API Melhor Envio"

        return {
            "mensagem": error_msg
        }, 400