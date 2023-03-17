from tkinter import *
import tkinter as tk
import customtkinter as ct
from PIL import Image, ImageTk
from customtkinter import CTkLabel

ct.set_appearance_mode('dark')
ct.set_default_color_theme('dark-blue')

window = ct.CTk()
window.geometry('700x400')
window.resizable(False, False)
window.title('Login System')

# imagem da tela inicial

image = Image.open('assets/img/login.png')
new_size = (340, 200)
image = image.resize(new_size)

img = ImageTk.PhotoImage(image)

label_img = ct.CTkLabel(master=window, image=img)
label_img.place(x=5, y=150)

frame = ct.CTkFrame(master=window, width=350, height=396)
frame.pack(side=RIGHT)

label_tt = ct.CTkLabel(master=window, text='Entre em sua conta!', font=('Roboto', 30, 'bold'), text_color='Blue').place(x=45, y=40)

# frame widgets

def alternar_senha():
    if var.get():
        entry2.configure(show='')
    else:
        entry2.configure(show='*')


label = ct.CTkLabel(master=frame, text='Sistema de Login', font=(
    'Roboto', 24), text_color='white', justify='center')
label.place(x=85, y=40)

entry1 = ct.CTkEntry(master=frame, placeholder_text='Nome do Usuário',
                     width=300, font=('Roboto', 14)).place(x=25, y=105)
label1 = ct.CTkLabel(master=frame, text='*Nome de usuário obrigatório.',
                     text_color='gray', font=('Roboto', 9)).place(x=28, y=133)

entry2 = ct.CTkEntry(master=frame,
                     placeholder_text='Senha do Usuário',
                     width=300,
                     font=('Roboto', 14),
                     show='*')
entry2.place(x=25, y=175)
label2 = ct.CTkLabel(master=frame, text='*Senha obrigatória.',
                     text_color='gray', font=('Roboto', 9)).place(x=28, y=203)


var = BooleanVar()
check_btn = ct.CTkCheckBox(master=frame,
                              text='Mostrar Senha',
                              variable=var,
                              command=alternar_senha)
check_btn.place(x=28, y=235)

button = ct.CTkButton(master=frame, text="LOGIN", width=300).place(x=25, y=285)


window.mainloop()
