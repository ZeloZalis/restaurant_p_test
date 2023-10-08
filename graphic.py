from tkinter import *
from tkinter import colorchooser as CC
from tkinter import messagebox as MB
from tkinter import font
import sqlite3

root = Tk()
root.title('Restaurant Raftel - Menú')
root.geometry('400x600')
root.resizable(0, 0)
root.config(background='#FFF3F1')

back = Frame(root, width=390, height=590)
back.config(relief='sunken', bd=20)
back.config(background='#FFF3F1')
back.pack_propagate(False)
back.pack(anchor=CENTER)

label_font = font.Font(size = 27)
title = Label(back, text='Menú', background='#FFF3F1', font=label_font)
title.pack(anchor=N)

table = sqlite3.connect('restaurante.db')
cursor = table.cursor()
cursor.execute('SELECT * FROM categoria')
categorias = cursor.fetchall()
sum = 0
for n in categorias:
    texto_font = font.Font(size = 15)
    texto_cat = Label(back, text=f'{n[1]}', background='#FFF3F1', font=texto_font)
    texto_cat.pack(anchor=S)
    cursor.execute(f'SELECT * FROM plato WHERE categoria_id = {sum+1}')
    sum+=1
    platos = cursor.fetchall()
    for i in platos:
        texto2_font = font.Font(size = 10)
        texto2 = Label(back, text=f'{i[1]}', background='#FFF3F1', font=texto2_font)
        texto2.pack(anchor=S)
root.mainloop()