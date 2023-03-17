from tkinter import *
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from customtkinter import CTkLabel

window =ctk.CTk()

class Application():
    def __init__(self):
        self.window = window
        self.theme()
        self.display()
        self.login_screen()
        window.mainloop()


    def theme(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def display(self):
        window.geometry('700x400')
        window.resizable(False, False)
        window.title('Login System')
        window.iconphoto(False, PhotoImage(file='assets/img/login.png'))

    def login_screen(self):
    # imagem da tela inicial

        image = Image.open('assets/img/login.png')
        new_size = (340, 200)
        image = image.resize(new_size)

        img = ImageTk.PhotoImage(image)

        label_img = ctk.CTkLabel(master=window, image=img, text=None)
        label_img.place(x=5, y=150)

        #frame

        login_frame = ctk.CTkFrame(master=window, width=350, height=396)
        login_frame.pack(side=RIGHT)

        label_tt = ctk.CTkLabel(master=window, text='Entre em sua conta!', font=('Roboto', 30, 'bold'), text_color='#7091D8').place(x=45, y=40)

        # frame widgets

        def alternar_senha():
            if var.get():
                password_entry.configure(show='')
            else:
                password_entry.configure(show='*')


        title_label = ctk.CTkLabel(master=login_frame, text='Sistema de Login', font=(
            'Roboto', 24), text_color='white', justify='center').place(x=85, y=40)

        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text='Nome do Usuário',
                            width=300, font=('Roboto', 14)).place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame, text='*Nome de usuário obrigatório.',
                            text_color='gray', font=('Roboto', 9)).place(x=28, y=133)

        password_entry = ctk.CTkEntry(master=login_frame,
                            placeholder_text='Senha do Usuário',
                            width=300,
                            font=('Roboto', 14),
                            show='*').place(x=25, y=175)
        password_label = ctk.CTkLabel(master=login_frame, text='*Senha obrigatória.',
                            text_color='gray', font=('Roboto', 9)).place(x=28, y=203)


        var = BooleanVar()
        check_btn = ctk.CTkCheckBox(master=login_frame,
                                    text='Mostrar Senha',
                                    variable=var,
                                    command=alternar_senha).place(x=28, y=235)

        login_button = ctk.CTkButton(master=login_frame, text="LOGIN", width=300).place(x=25, y=285)
        register_button = ctk.CTkButton(master=login_frame, text="REGISTER", width=300, fg_color='green', hover_color='#2D5000').place(x=25, y=325)
        register_span = ctk.CTkLabel(master=login_frame, text='Não tem uma conta? Cadastre-se!', font=("Roboto", 12)).place(x=25, y=360)

Application()