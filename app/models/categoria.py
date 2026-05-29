#Tabela de categoria 

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome  = Column(String(100), nullable=False, unique=True)
    ativo = Column(Boolean, default=True)

    #relacionameto com a tabela de produtos
    #Lazy="select" - carrega os prodtutos apenas quando necessário.
    produtos = relationship("Produto", back_populates="categoria", lazy="select")
