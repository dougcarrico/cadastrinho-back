from sqlalchemy import Column, String, Integer, DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from datetime import datetime
from typing import Union

from model import Base

class Produto(Base):
    """
   Classe que define a tabela Produto
    """

    __tablename__ = 'produto'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(150), unique=True)
    quantidade: Mapped[int]
    tipo: Mapped[str] = mapped_column(String(100))
    data_incersao: Mapped[datetime] = mapped_column(DateTime)
    data_atualizacao: Mapped[datetime] = mapped_column(DateTime)

    def __init__(self, nome:str, quantidade:int, tipo:str):

        """
        Cria um produto

        Argumentos:
            nome: nome do produto.
            quantidade: quantidade de produtos em estoque.
            tipo: tipo do produto.
        """
        self.nome = nome
        self.quantidade = quantidade
        self.tipo = tipo
        self.data_incersao = datetime.now()
        self.data_atualizacao = self.data_incersao