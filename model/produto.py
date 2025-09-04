from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True)
    nome = Column(String(150), unique=True)
    quantidade = Column(Integer)
    tipo = Column(String(100))
    data_insercao = Column(DateTime, default=datetime.now())
    data_atualizacao = Column(DateTime, default=datetime.now())


    def __init__(self, nome:str, quantidade:int, tipo:str, data_insercao:DateTime):
        """
        Cria um produto

        Arguments:
            nome: nome do produto.
            quantidade: quantidade de produtos em estoque.
            tipo: tipo do produto.
            data_insercao: data que o produto foi inserido no banco de dados
            data_atualizacao: data da última atualização do produto no banco de dados
        """

        self.nome == nome
        self.quantidade == quantidade
        self.tipo == tipo
        self.data_insercao == data_insercao