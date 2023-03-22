import customtkinter as ctk
from tkinter import PhotoImage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.homescreen_config()
        self.login_screen()

    # Configuração da janela principal

    def homescreen_config(self):
        self.geometry('700x400')
        self.title('Sistema de Login')
        self.resizable(False, False)

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
        self.confirm_username_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Cadastre seu usuário', font=('Century Gothic bold', 16), corner_radius=15, border_color='#407bff')
        self.confirm_username_entry.grid(row=2, column=0, padx=10, pady=10)

        self.label_password_description = ctk.CTkLabel(self.frame_register, text='*Campo obrigatório', font=('Century Gothic bold', 10)).place(x=15, y=193)
        self.password_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Cadastre sua senha', font=('Century Gothic bold', 16), corner_radius=15, border_color='#407bff', show='*')
        self.password_register_entry.grid(row=3, column=0, padx=10, pady=10)
    
        # Campo de confirmação de senha
        self.label_password_description = ctk.CTkLabel(self.frame_register, text='*Campo obrigatório', font=('Century Gothic bold', 10)).place(x=15, y=246)
        self.confirm_password_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text='Confirme sua senha', font=('Century Gothic bold', 16), corner_radius=15, border_color='#407bff', show='*')
        self.confirm_password_entry.grid(row=4, column=0, padx=10, pady=15)

        self.span = ctk.CTkLabel(self.frame_register, text='')
        self.span.grid(row=5, column=0, padx=10, pady=8)

        self.show_password = ctk.CTkCheckBox(self.frame_register, text='Mostrar senha', font=('Century Gothic bold', 12)).place(x=15, y=275)


        self.button_register = ctk.CTkButton(self.frame_register, width=300, text='Inscreva-se', font=('Century Gothic bold', 16), corner_radius=15, command=self.register_screen, fg_color='green', hover_color='#050')
        self.button_register.grid(row=7, column=0, padx=10,)

        self.button_login_back = ctk.CTkButton(self.frame_register, width=300, text='Voltar', font=('Century Gothic bold', 16), corner_radius=15, fg_color='#444', hover_color='#333', command=lambda:(self.frame_register.place_forget(), (App.login_screen(self))))
        self.button_login_back.grid(row=8, column=0, padx=10, pady=10)

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

        self.button_login = ctk.CTkButton(self.frame_login, width=300, text='Login', font=('Century Gothic bold', 16), corner_radius=15, fg_color='green', hover_color='#050')
        self.button_login.grid(row=4, column=0, padx=10, pady=10)

        self.button_register = ctk.CTkButton(self.frame_login, width=300, text='Inscreva-se', font=('Century Gothic bold', 16), corner_radius=15, command=self.register_screen)
        self.button_register.grid(row=5, column=0, padx=10, pady=10)

        self.span = ctk.CTkLabel(self.frame_login, text='Não possui uma conta? Inscreva-se!', font=('Century Gothic', 10))
        self.span.grid(row=6, column=0, padx=10, pady=1)

if __name__ == '__main__':
    app = App()
    app.mainloop()