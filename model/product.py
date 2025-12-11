from sqlalchemy import Column, String, Integer, DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from datetime import datetime
from typing import Union

from model import Base

class Product(Base):
    """
   Classe que define a tabela Produto
    """

    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True)
    quantity: Mapped[int]
    type: Mapped[str] = mapped_column(String(100))
    date_created: Mapped[datetime] = mapped_column(DateTime)
    date_updated: Mapped[datetime] = mapped_column(DateTime)

    def __init__(self, name:str, quantity:int, type:str):

        """
        Cria um produto

        Argumentos:
            name: nome do produto.
            quantity: quantidade de produtos em estoque.
            type: tipo do produto.
        """
        self.name = name
        self.quantity = quantity
        self.type = type
        self.date_created = datetime.now()
        self.date_updated = self.date_created