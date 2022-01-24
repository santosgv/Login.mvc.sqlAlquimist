from Model import Usuario,retornaSession

session = retornaSession()

class CadastroDao:
    @classmethod
    def ler(cls):
        session=retornaSession()
        usuarios =session.query(Usuario).all()

        for i in usuarios:
            user = (i.nome,i.email,i.senha)

        return user[0],user[1],user[2]

    @classmethod
    def salvar(cls ,nome ,email,senha):
        session = retornaSession()
        user = Usuario(nome=nome,
                       email=email,
                       senha=senha)
        session.add(user)
        session.commit()


a=CadastroDao()
a.ler()