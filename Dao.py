from Model import Usuario,retornaSession

session = retornaSession()

class CadastroDao:
    @classmethod
    def ler(cls):
        session=retornaSession()
        usuarios =session.query(Usuario).all()
        user = []
        for i in usuarios:
            user.append(i)
        return user


    @classmethod
    def salvar(cls ,nome ,email,senha):
        session = retornaSession()
        user = Usuario(nome=nome,
                       email=email,
                       senha=senha,
                       ativo=True)
        session.add(user)
        session.commit()

