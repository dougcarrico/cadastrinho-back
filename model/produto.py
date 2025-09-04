from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from datetime import datetime

from model import Base

class Produto(Base):
    __tablename__ = 'produto'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(150), unique=True)
    quantidade: Mapped[int] = mapped_column(Integer)
    tipo: Mapped[str] = mapped_column(String(100))
    data_insercao: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    data_atualizacao: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())


    def __init__(self, nome:str, quantidade:int, tipo:str):
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