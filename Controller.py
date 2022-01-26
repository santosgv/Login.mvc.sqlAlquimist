from Dao import CadastroDao,logarDao
import re
import hashlib

class controllerCadastro:
    @classmethod

    def verificaDados(cls, nome, email, senha):
        '''
        :param nome:
        :param email:
        :param senha:
        :return: 1 Cadastro realizado com sucesso
        :return: 2 quantidade minima de letras no nome
        :return: 3 Email invalido
        :return: 4 Senha precisa ser forte
        '''
        if len(nome) < 5 or len(nome) > 100:
            return 2
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return 3
        if not re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#])(?:([0-9a-zA-Z$*&@#])(?!\1)){8,}$", senha):
            return 4
        return 1


    def cadastrarUsuario(cls, nome, email, senha):
        '''
        :param nome:
        :param email:
        :param senha:
        :return: 1 Cadastro realizado com sucesso
        :return: 2 quantidade minima de letras no nome
        :return: 3 Email invalido
        :return: 4 Senha precisa ser forte
        :return: 5 Email ja cadastrado
        :return: 6 Erro interno do sistema
        '''
        usuario = CadastroDao.ler(email)

        if len(usuario) > 0:
            return 5

        dados_verificados = cls.verificaDados(nome,email,senha)

        if dados_verificados != 1:
            return dados_verificados

        try:
            senha =hashlib.sha256(senha.encode()).hexdigest()
            CadastroDao.salvar(nome, email, senha)
            return 1
        except:
            return 6

class controllerLogar:
    def logaSistema(cls,email,senha):
        '''
        :param email: Email
        :param senha: Senha
        :return: 1 usuario ou senha invalido
        :return: 2 Login realizado com sucesso
        '''
        senha = hashlib.sha256(senha.encode()).hexdigest()
        x = logarDao.logar(email,senha)
        if len(x) == 0:
            return 1
        else:
            return 2

