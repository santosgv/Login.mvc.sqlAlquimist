from Dao import CadastroDao
import re

class controllerCadastro:
    def cadastrarUsuario(self, nome, email, senha):
        x = CadastroDao.ler()
        existe = False
        for i in x:
            if i.nome == nome or i.email == email:
                existe =True
                print('Ja existem um usuario com estes dados no sistema')

        if len(nome) < 5:
            print('O nome precisa ser maior que 5 caracteres')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print('Digite um email valido')

        if not re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#])(?:([0-9a-zA-Z$*&@#])(?!\1)){8,}$",senha):
            print('''Sua senha precisa ser Forte !!!
                deve conter ao menos um dígito
            * deve conter ao menos uma letra minúscula         
            * deve conter ao menos uma letra maiúscula         
            * deve conter ao menos um caractere especial       
            * deve conter ao menos 8 dos caracteres mencionados
                    ''')

        if  existe == False :
            CadastroDao.salvar(nome, email, senha)
            print('Cadastrado com sucesso')

    def logaSistema(self):