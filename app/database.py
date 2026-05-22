from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

#Carregar as variaveis de ambiente
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Classe base
class Base(DeclarativeBase):
    pass

#funcao de conexao
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()