from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session
from model import Produto
from schemas import *
from flask_cors import CORS

info = Info(title="API Cadastrinho", version="0.0.1")
app = OpenAPI(__name__, info=info)
CORS(app)

#definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
produto_tag = Tag(name="Produto", description="Adição de produto")

@app.get('/', tags=[home_tag])
def home():
    """
    Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema})

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
        error_msg = f"Erro de integridade: {e.orig}"
        return {
            "message": error_msg
        }, 400