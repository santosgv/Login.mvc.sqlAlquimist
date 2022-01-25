from Dao import CadastroDao
import re

class controllerCadastro:
    def cadastrarUsuario(self, nome, email, senha):
        '''

        :param nome:
        :param email:
        :param senha:
        :return:
        '''
        x = CadastroDao.ler()
        existe = False
        for i in x:
            if i.nome == nome or i.email == email and i.ativo == 1:
                existe =True
                return existe and 1
        if len(nome) < 5:
            existe = False
            return 1 and existe

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            existe = False
            return 2 and existe

        if not re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#])(?:([0-9a-zA-Z$*&@#])(?!\1)){8,}$", senha):
            existe = False
            return 3 and existe

        if  existe == False:
            CadastroDao.salvar(nome, email, senha)
            return 4

class controllerLogar:
    def logaSistema(self,email,senha):
        '''

        :param email:
        :param senha:
        :return:
        '''
        x = CadastroDao.logar(email,senha)
        if len(x) == 0:
            return 1
        else:
            return 2
