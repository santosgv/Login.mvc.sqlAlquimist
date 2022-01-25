from sqlalchemy import  create_engine , Column , Integer , String ,BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine =create_engine('sqlite:///Usuaios.db' , echo=True)
Session= sessionmaker(bind=engine)
Base =declarative_base()

def retornaSession():
    engine =create_engine('sqlite:///Usuaios.db' , echo=True)
    Session= sessionmaker(bind=engine)

    return Session()

class Usuario(Base):
    __tablename__ ="Usuaio"
    id = Column(Integer , primary_key=True)
    nome = Column(String(50))
    email = Column(String(50))
    senha = Column(String(50))
    ativo = Column(BOOLEAN)


Base.metadata.create_all(engine)
