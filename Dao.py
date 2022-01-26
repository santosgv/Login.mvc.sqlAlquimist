from Model import Usuario,retornaSession

session = retornaSession()

class CadastroDao:
    @classmethod
    def ler(cls ,email):
        session=retornaSession()
        usuarios =session.query(Usuario).filter(Usuario.email == email).all()
        user = []
        for i in usuarios:
            user.append(i)
        return user


    @classmethod
    def salvar(cls ,nome ,email,senha):
        session = retornaSession()
        user = Usuario(nome=str(nome),
                       email=str(email),
                       senha=str(senha),
                       ativo=True)
        session.add(user)
        session.commit()

class logarDao:
    @classmethod
    def logar(cls,email,senha):
        session =retornaSession()
        login = session.query(Usuario).filter(Usuario.email == email).filter(Usuario.senha == senha)
        log = []
        for i in login:
            log.append(i)
        return log
