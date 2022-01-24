from Model import  Usuario,retornaSession

session = retornaSession()

class CadastroDao:
    @classmethod
    def ler(cls):
        session=retornaSession()
        usuarios =session.query(Usuario).all()

        for i in usuarios:
            print(i.nome,i.email,i.senha)

    @classmethod
    def salvar(cls):
        ...


a=CadastroDao()
a.ler()