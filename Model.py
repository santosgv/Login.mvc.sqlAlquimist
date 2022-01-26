from sqlalchemy import  create_engine , Column , Integer , String ,BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine =create_engine('sqlite:///Usuarios.db' , echo=True)
Session= sessionmaker(bind=engine)
Base =declarative_base()

def retornaSession():
    engine =create_engine('sqlite:///Usuarios.db' , echo=True)
    Session= sessionmaker(bind=engine)

    return Session()

class Usuario(Base):
    __tablename__ ="Usuario"
    id = Column(Integer , primary_key=True)
    nome = Column(String(100))
    email = Column(String(50))
    senha = Column(String(100))
    ativo = Column(BOOLEAN)


Base.metadata.create_all(engine)
