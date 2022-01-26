from tkinter import *
from Controller import controllerCadastro,controllerLogar

main = Tk()

class validacao():
    def logar(self):
        login = self.login.get()
        password = self.password.get()

        user =controllerLogar()
        if user.logaSistema(login,password) == 1:
            self.lbStatus['text']= ('Email ou senha incorreto')

        elif user.logaSistema(login,password) == 2:
            self.lbStatus['text']= ('Login efetuado com sucesso')

    def cadastrar(self):
        nome = self.entNomeUsuario.get()
        email = self.entEmailUsuario.get()
        senha = self.entSenhausuario.get()

        user = controllerCadastro()

        if user.cadastrarUsuario(nome,email,senha) == 2:
            self.lbAlerta['text'] ='O nome precisa ser maior que 5 caracteres'
        if user.cadastrarUsuario(nome, email, senha) == 3:
            self.lbAlerta['text'] ='Digite um email valido'
        if user.cadastrarUsuario(nome, email, senha) == 4:
            self.lbAlerta['text'] = ('''Sua senha precisa ser Forte !!!
            * deve conter ao menos uma letra minúscula         
            * deve conter ao menos uma letra maiúscula         
            * deve conter ao menos um caractere especial       
            * deve conter ao menos 8 dos caracteres mencionados
                    ''')
        if user.cadastrarUsuario(nome, email, senha) == 5:
            self.lbAlerta['text'] = 'Email ja utilizado no sistema'

        if user.cadastrarUsuario(nome, email, senha) == 1:
            self.lbAlerta['text'] = 'Cadastrado com Sucesso'




class Aplicacao(validacao):
    def __init__(self):
        self.main = main
        self.principal()
        self.frame()
        self.label()
        main.mainloop()

    def principal(self):
        self.main.title('Sistema de Login ORM')
        self.main.geometry('800x500')
        self.main.resizable(False, False)

    def frame(self):
        self.framePrincipal = Frame(self.main, bg='#F8F8FF', highlightbackground='black')
        self.framePrincipal.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def label(self):
        Label(self.framePrincipal, text='Login', bg='white', fg='#B22222').place(relx=0.25, rely=0.30)
        self.login = Entry(self.framePrincipal)
        self.login.place(relx=0.35, rely=0.30,width=200)

        Label(self.framePrincipal, text='Senha', bg='white' ,fg='#B22222').place(relx=0.25, rely=0.40)
        self.password = Entry(self.framePrincipal,show="*")
        self.password.place(relx=0.35, rely=0.40,width=200)

        self.lbStatus=Label(self.framePrincipal, text='', bg='white', fg='#B22222')
        self.lbStatus.place(relx=0.35, rely=0.60)

        Button(self.framePrincipal,text='Logar', bg='white',fg='#B22222',command=self.logar).place(relx=0.35, rely=0.48)
        Button(self.framePrincipal, text='Cadastrar', bg='white', fg='#B22222', command=self.iCadastro).place(relx=0.48, rely=0.48)

    def iCadastro(self):
        nwwindow = Toplevel(self.framePrincipal, bg='white')
        nwwindow.geometry('400x400')
        nwwindow.title('Novo Usuario')
        nwwindow.resizable(False, False)

        Label(nwwindow, text='Nome', bg='white').place(relx=0.10, rely=0.10)
        self.entNomeUsuario = Entry(nwwindow)
        self.entNomeUsuario.place(relx=0.35, rely=0.10)

        Label(nwwindow, text='Email', bg='white').place(relx=0.10, rely=0.20)
        self.entEmailUsuario = Entry(nwwindow)
        self.entEmailUsuario.place(relx=0.35, rely=0.20)

        Label(nwwindow, text='Senha', bg='white').place(relx=0.10, rely=0.30)
        self.entSenhausuario = Entry(nwwindow,show="*")
        self.entSenhausuario.place(relx=0.35, rely=0.30)

        self.lbAlerta =Label (nwwindow,text='',bg='white')
        self.lbAlerta.place(relx=0.01, rely=0.40)
        self.btCadastroUsuario = Button(nwwindow, text='Cadastrar Usuario', bg='green',command=self.cadastrar)
        self.btCadastroUsuario.place(relx=0.30, rely=0.80)


Aplicacao()

