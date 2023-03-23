import customtkinter as ctk
from tkinter import messagebox
from tkinter import *
import sqlite3
    
class BackEnd():

    def drop_table(self):
        self.connect_db()
        self.cursor.execute("DROP TABLE IF EXISTS Users;")
        self.connect.commit()
        self.disconnect_db()
        print('Tabela excluída com sucesso!')

    def clear_register_entry(self):
        self.username_register_entry.delete(0, END)
        self.email_register_entry.delete(0, END)
        self.password_register_entry.delete(0, END)
        self.confirm_password_register_entry.delete(0, END)

    def connect_db(self):
        self.connect = sqlite3.connect('Register_system.db')
        self.cursor = self.connect.cursor()
        print('Banco de dados conectado com sucesso!')

    def disconnect_db(self):
        self.connect.close()
        print('Banco de dados desconectado')

    def create_table(self):
        self.connect_db()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL,
            Email TEXT NOT NULL,
            Password TEXT NOT NULL,
            Confirm_Password TEXT NOT NULL
        );
        ''')
        self.connect.commit()
        print('Tabela criada com sucesso!')
        self.disconnect_db()

    def register_user(self):
        self.username_register = self.username_register_entry.get()
        self.email_register = self.email_register_entry.get()
        self.password_register = self.password_register_entry.get()
        self.confirm_password_register = self.confirm_password_register_entry.get()

        self.connect_db()

        self.cursor.execute('''
            INSERT INTO Users (Username, Email, Password, Confirm_Password)
            VALUES (?, ?, ?, ?)''', (self.username_register, self.email_register, self.password_register, self.confirm_password_register))

        try:
            if (self.username_register == "" or self.email_register == '' or self.password_register == '' or self.confirm_password_register == ''):

                messagebox.showerror(title='Sistema de Login', message='Por favor, preencha todos os campos!')

            elif(len(self.username_register) < 3):

                messagebox.showwarning(title='Sistema de Login', message='O usuário deve ter pelo menos 3 caracteres.')

            elif(len(self.password_register) < 4):

                messagebox.showwarning(title='Sistema de Login', message='A sua senha deve ter pelo menos 4 dígitos.')

            elif (self.password_register != self.confirm_password_register):

                messagebox.showerror(title='Sistema de Login', message='ERRO\nAs senhas não são iguais.')

            else:
                self.connect.commit()
                messagebox.showinfo(title='Sistema de Login', message=f'Parabéns {self.username_register}!\nOs seus dados foram cadastrados com sucesso!')
                self.disconnect_db
                self.clear_register_entry()

        except:
            messagebox.showerror(title='Sistema de Login', message='Erro no processamento do seu cadastro\nPor favor, tente novamente.')
            self.disconnect_db

    def verify_login(self):
        self.username_login = self.username_login_entry.get()
        self.password_login = self.password_login_entry.get()

        self.connect_db()

        self.cursor.execute('''SELECT * FROM Users WHERE (Username = ? AND Password = ?)''', (self.username_login, self.password_login))

        self.verify_db = self.cursor.fetchone()
        
        
        try:
            if (self.username_login == '' or self.password_login == ''):
                messagebox.showwarning(title='Sistema de Login', message='Preencha todos os campos!')
                
            if(self.username_login in self.verify_db and self.password_login in self.verify_db):

                messagebox.showinfo(title='Sistema de Login', message=f'Parabéns {self.username_login}!\nLogin feito com sucesso.')
                self.disconnect_db()
                self.clear_login_entry()

        except:
            messagebox.showerror(title='Sistema de Login', message='ERRO!\nUsuário ou senha estão incorretos.')
            self.disconnect_db()

class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.homescreen_config()
        self.login_screen()
        self.create_table()
         
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        # Excluir a tabela e desconectar o banco de dados
        self.drop_table()
        self.disconnect_db()
        self.destroy()

    # Configuração da janela principal
    def homescreen_config(self):
        self.geometry('700x400')
        self.title('Sistema de Login')
        self.resizable(False, False)


    def login_screen(self):

        # Imagens
        self.img = PhotoImage(file='assets/img/login.png')
        self.img = self.img.subsample(6, 6) # Reduzir a imagem para metade do tamanho original
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img).place(x=20, y=30)

        # Titulo
        self.title = ctk.CTkLabel(self, text='Seja bem-vindo(a)!', font=('Century Gothic bold', 24))
        self.title.grid(row=0, column=0, pady=30, padx=60)

        # Frame do formulário de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=365, y=10)

        # Widgets dentro do formulário de login
        self.label_title = ctk.CTkLabel(self.frame_login, text='Faça o seu Login', font=('Century Gothic bold', 24))
        self.label_title.grid(row=0, column=0, padx=10, pady=30)

        self.label_username_description = ctk.CTkLabel(self.frame_login, text='*Campo obrigatório', font=('Century Gothic bold', 10)).place(x=15, y=130)
        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text='Nome de usuário', font=('Century Gothic bold', 16), corner_radius=15, border_color='#407bff')
        self.username_login_entry.grid(row=1, column=0, padx=10, pady=15)
       
        self.label_password_description = ctk.CTkLabel(self.frame_login, text='*Campo obrigatório', font=('Century Gothic bold', 10)).place(x=15, y=189)
        self.password_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text='Senha', font=('Century Gothic bold', 16), corner_radius=15, border_color='#407bff', show='*')
        self.password_login_entry.grid(row=2, column=0, padx=10, pady=15)

        self.span = ctk.CTkLabel(self.frame_login, text='')
        self.span.grid(row=3, column=0, padx=10, pady=10)
        self.show_password = ctk.CTkCheckBox(self.frame_login, text='Mostrar senha', font=('Century Gothic bold', 12)).place(x=15, y=220)

        self.button_login = ctk.CTkButton(self.frame_login, width=300, text='Login', font=('Century Gothic bold', 16), corner_radius=15, fg_color='green', hover_color='#050', command=self.verify_login)
        self.button_login.grid(row=4, column=0, padx=10, pady=10)

        self.button_register = ctk.CTkButton(self.frame_login, width=300, text='Inscreva-se', font=('Century Gothic bold', 16), corner_radius=15, command=self.register_screen)
        self.button_register.grid(row=5, column=0, padx=10, pady=10)

        self.span_login = ctk.CTkLabel(self.frame_login, text='Não possui uma conta? Inscreva-se!', font=('Century Gothic', 10))
        self.span_login.grid(row=6, column=0, padx=10, pady=1)

    def register_screen(self):

        # Adiciona o frame do formulário de cadastro
        self.frame_register = ctk.CTkFrame(self, width=350, height=380)
        self.frame_register.place(x=365, y=7)

        # Remove o formulário de login
        self.frame_login.place_forget()

        # Criando o titulo
        self.label_title = ctk.CTkLabel(self.frame_register, text='Faça o seu Cadastro', font=('Century Gothic bold', 24))
        self.label_title.grid(row=0, column=0, padx=10, pady=18)

        # Campo de cadastro
        self.label_email_description = ctk.CTkLabel(self.frame_register, text='*Campo obrigatório', font=('Century Gothic bold', 10)).place(x=15, y=97)
        self.email_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Cadastre seu email', font=('Century Gothic bold', 16), corner_radius=15, border_color='#407bff')
        self.email_register_entry.grid(row=1, column=0, padx=10, pady=10)

        self.label_username_description = ctk.CTkLabel(self.frame_register, text='*Campo obrigatório', font=('Century Gothic bold', 10)).place(x=15, y=145)
        self.username_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Cadastre seu usuário', font=('Century Gothic bold', 16), corner_radius=15, border_color='#407bff')
        self.username_register_entry.grid(row=2, column=0, padx=10, pady=10)

        self.label_password_description = ctk.CTkLabel(self.frame_register, text='*Campo obrigatório', font=('Century Gothic bold', 10)).place(x=15, y=193)
        self.password_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Cadastre sua senha', font=('Century Gothic bold', 16), corner_radius=15, border_color='#407bff', show='*')
        self.password_register_entry.grid(row=3, column=0, padx=10, pady=10)
    
        # Campo de confirmação de senha
        self.label_password_description = ctk.CTkLabel(self.frame_register, text='*Campo obrigatório', font=('Century Gothic bold', 10)).place(x=15, y=246)
        self.confirm_password_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Confirme sua senha', font=('Century Gothic bold', 16), corner_radius=15, border_color='#407bff', show='*')
        self.confirm_password_register_entry.grid(row=4, column=0, padx=10, pady=15)

        self.span_register = ctk.CTkLabel(self.frame_register, text='')
        self.span_register.grid(row=5, column=0, padx=10, pady=8)

        self.show_password = ctk.CTkCheckBox(self.frame_register, text='Mostrar senha', font=('Century Gothic bold', 12)).place(x=15, y=275)


        self.button_register = ctk.CTkButton(self.frame_register, width=300, text='Inscreva-se', font=('Century Gothic bold', 16), corner_radius=15, command=self.register_user, fg_color='green', hover_color='#050')
        self.button_register.grid(row=7, column=0, padx=10,)

        self.button_login_back = ctk.CTkButton(self.frame_register, width=300, text='Voltar', font=('Century Gothic bold', 16), corner_radius=15, fg_color='#444', hover_color='#333', command=lambda:(self.frame_register.place_forget(), (App.login_screen(self))))
        self.button_login_back.grid(row=8, column=0, padx=10, pady=10)


    def clear_register_entry(self):
        self.username_register_entry.delete(0, END)
        self.email_register_entry.delete(0, END)
        self.password_register_entry.delete(0, END)
        self.confirm_password_register_entry.delete(0, END)

    def clear_login_entry(self):
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)


if __name__ == '__main__':
    app = App()
    app.mainloop()